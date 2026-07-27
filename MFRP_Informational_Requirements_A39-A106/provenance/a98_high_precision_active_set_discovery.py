#!/usr/bin/env python3
"""Discovery-only 180-digit revised-simplex solve for A98.

The output identifies a candidate basis for later independent exact-rational
certification.  No scientific claim relies on floating/high-precision discovery.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 180
M = 396
H = M // 2
COUNT = M + 1
S = mp.mpf(13) / 100
MEAN = mp.mpf(M) / 2
EPS = mp.mpf(1) / (mp.mpf(1875) * mp.power(2, H))
TARGET = mp.mpf(1) / 2
BETA = mp.mpf(1) / 8
GAMMA = mp.mpf(1) / 16
T_INDEX = 2 * COUNT
SLACK_START = T_INDEX + 1
ARTIFICIAL_START = SLACK_START + 6
ORIGINAL_VARIABLE_COUNT = ARTIFICIAL_START
ROW_COUNT = 11
TOTAL_VARIABLE_COUNT = ARTIFICIAL_START + 5


def build_columns():
    columns = []
    for x in range(COUNT):
        columns.append([
            mp.mpf(1), 0, mp.mpf(x), 0, 0,
            S**x, -(S**x), BETA**x, -(BETA**x), GAMMA**x, -(GAMMA**x),
        ])
    for x in range(COUNT):
        columns.append([
            0, mp.mpf(1), 0, mp.mpf(x), TARGET**x,
            -(S**x), S**x, -(BETA**x), BETA**x, -(GAMMA**x), GAMMA**x,
        ])
    columns.append([
        -1, -1, -MEAN, -MEAN, 0,
        -2 * EPS, -2 * EPS, -2 * EPS, -2 * EPS, -2 * EPS, -2 * EPS,
    ])
    for row in range(6):
        column = [mp.mpf(0)] * ROW_COUNT
        column[5 + row] = 1
        columns.append(column)
    for row in range(5):
        column = [mp.mpf(0)] * ROW_COUNT
        column[row] = 1
        columns.append(column)
    return columns


COLUMNS = build_columns()
RHS = mp.matrix([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])


def basis_inverse(indices):
    matrix = mp.matrix([[COLUMNS[j][i] for j in indices] for i in range(ROW_COUNT)])
    inverse = mp.inverse(matrix)
    return inverse, inverse * RHS


def revised_simplex(objective, basis, allowed, tolerance=mp.mpf("1e-140"), maximum_iterations=5000):
    iterations = 0
    while iterations < maximum_iterations:
        inverse, basic = basis_inverse(basis)
        basic_objective = mp.matrix([objective[j] for j in basis])
        dual = inverse.T * basic_objective
        basis_set = set(basis)
        entering = None
        best_reduced_cost = None
        for column_index in allowed:
            if column_index in basis_set:
                continue
            reduced_cost = objective[column_index] - mp.fdot(dual, mp.matrix(COLUMNS[column_index]))
            if reduced_cost > tolerance and (
                best_reduced_cost is None or reduced_cost > best_reduced_cost
            ):
                entering = column_index
                best_reduced_cost = reduced_cost
        if entering is None:
            return basis, inverse, basic, mp.fdot(basic_objective, basic), iterations
        direction = inverse * mp.matrix(COLUMNS[entering])
        ratio = None
        leaving_position = None
        for i in range(ROW_COUNT):
            if direction[i] > tolerance:
                candidate = basic[i] / direction[i]
                if ratio is None or candidate < ratio - tolerance or (
                    abs(candidate - ratio) <= tolerance and basis[i] < basis[leaving_position]
                ):
                    ratio = candidate
                    leaving_position = i
        if leaving_position is None:
            raise RuntimeError("unbounded discovery LP")
        basis[leaving_position] = entering
        iterations += 1
    raise RuntimeError("simplex iteration limit")


def main():
    basis = list(range(ARTIFICIAL_START, ARTIFICIAL_START + 5)) + list(
        range(SLACK_START, SLACK_START + 6)
    )
    phase_one_objective = [mp.mpf(0)] * TOTAL_VARIABLE_COUNT
    for j in range(ARTIFICIAL_START, ARTIFICIAL_START + 5):
        phase_one_objective[j] = -1
    basis, inverse, basic, phase_one_value, phase_one_iterations = revised_simplex(
        phase_one_objective, basis, range(TOTAL_VARIABLE_COUNT)
    )
    if phase_one_value != 0:
        raise RuntimeError("phase one did not reach exact high-precision zero")

    # Degenerate artificial columns are pivoted out when necessary.
    for position, index in list(enumerate(basis)):
        if index < ARTIFICIAL_START:
            continue
        inverse, basic = basis_inverse(basis)
        basis_set = set(basis)
        replacement = None
        for candidate in range(ORIGINAL_VARIABLE_COUNT):
            if candidate in basis_set:
                continue
            coefficient = (inverse * mp.matrix(COLUMNS[candidate]))[position]
            if abs(coefficient) > mp.mpf("1e-130"):
                replacement = candidate
                break
        if replacement is None:
            raise RuntimeError("could not remove a phase-one artificial column")
        basis[position] = replacement

    phase_two_objective = [mp.mpf(0)] * TOTAL_VARIABLE_COUNT
    for x in range(COUNT):
        phase_two_objective[x] = TARGET**x
    basis, inverse, basic, phase_two_value, phase_two_iterations = revised_simplex(
        phase_two_objective, basis, range(ORIGINAL_VARIABLE_COUNT)
    )

    p_support = sorted(index for index in basis if 0 <= index < COUNT)
    q_support = sorted(index - COUNT for index in basis if COUNT <= index < 2 * COUNT)
    slack_names = ["alpha_plus", "alpha_minus", "beta_plus", "beta_minus", "gamma_plus", "gamma_minus"]
    positive_slacks = sorted(
        slack_names[index - SLACK_START]
        for index in basis if SLACK_START <= index < ARTIFICIAL_START
    )
    active_bands = [name for name in slack_names if name not in positive_slacks]

    record = {
        "audit": "A98_HIGH_PRECISION_ACTIVE_SET_DISCOVERY",
        "role": "discovery only; the proof is the independent exact rational A98 KKT certificate",
        "method": "two-phase revised simplex on the complete standard-form LP",
        "arithmetic": "mpmath, 180 decimal digits",
        "contract": {
            "maximum": M,
            "probe_s": "13/100",
            "epsilon": "1/(1875*2^198)",
            "full_atom_columns": 2 * COUNT,
            "Charnes_Cooper_scale_variable_count": 1,
            "band_slack_count": 6,
            "phase_one_artificial_count": 5,
            "standard_form_constraint_count": ROW_COUNT,
        },
        "phase_one": {
            "pivot_iterations": phase_one_iterations,
            "final_artificial_objective": mp.nstr(phase_one_value, 30),
        },
        "phase_two": {
            "pivot_iterations": phase_two_iterations,
            "discovered_standard_form_basis_indices": basis,
        },
        "index_map": {
            "p_x": f"0..{M}",
            "q_x": f"{COUNT}..{2*COUNT-1}",
            "t": T_INDEX,
            "slacks": {name: SLACK_START + i for i, name in enumerate(slack_names)},
        },
        "discovered_active_set": {
            "P_support": p_support,
            "Q_support": q_support,
            "active_bands": active_bands,
            "strictly_positive_inactive_slacks": positive_slacks,
        },
        "discovery_objective_decimal": mp.nstr(phase_two_value, 80),
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()

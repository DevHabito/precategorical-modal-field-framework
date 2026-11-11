#!/usr/bin/env python3
"""Exact finite regression for the random-2-order UPO substitution theorem.

The script independently:
1. enumerates simple permutations through n=9;
2. evaluates
       C_n = (n-1) + sum_{k=4}^n s_k * binom(n-1,k-1);
3. evaluates
       R_n = sum_{m=2}^n (n-m+1) C_m;
4. checks the counts against the prior exhaustive UPO recovery audits.

No Monte Carlo sampling is used.
"""

import itertools
import json
import math
from fractions import Fraction


def is_simple(pi):
    n = len(pi)

    if n < 4:
        return False

    for left in range(n):
        minimum = maximum = pi[left]

        for right in range(left, n):
            value = pi[right]
            minimum = min(minimum, value)
            maximum = max(maximum, value)
            size = right - left + 1

            if (
                2 <= size < n
                and maximum - minimum + 1 == size
            ):
                return False

    return True


simple_counts = {}

for n in range(4, 10):
    simple_counts[n] = sum(
        is_simple(pi)
        for pi in itertools.permutations(range(n))
    )


expected_simple = {
    4: 2,
    5: 6,
    6: 46,
    7: 338,
    8: 2926,
    9: 28146,
}

assert simple_counts == expected_simple


connected = {}

for n in range(2, 10):
    connected[n] = (
        n - 1
        + sum(
            simple_counts.get(k, 0)
            * math.comb(n - 1, k - 1)
            for k in range(4, n + 1)
        )
    )


expected_connected = {
    2: 1,
    3: 2,
    4: 5,
    5: 18,
    6: 101,
    7: 750,
    8: 6545,
    9: 64134,
}

assert connected == expected_connected


recoverable = {}

for n in range(2, 10):
    recoverable[n] = sum(
        (n - m + 1) * connected[m]
        for m in range(2, n + 1)
    )


expected_recoverable = {
    2: 1,
    3: 4,
    4: 12,
    5: 38,
    6: 165,
    7: 1042,
    8: 8464,
    9: 80020,
}

assert recoverable == expected_recoverable


rows = []

for n in range(2, 10):
    probability = Fraction(
        recoverable[n],
        math.factorial(n),
    )

    rows.append({
        "n": n,
        "simple_count": simple_counts.get(n),
        "connected_upo_count": connected[n],
        "recoverable_count": recoverable[n],
        "recovery_fraction": str(probability),
        "recovery_decimal": float(probability),
    })


result = {
    "audit": "RANDOM_2_ORDER_UPO_SUBSTITUTION_V1",
    "status": "PASS",
    "n_range": [2, 9],
    "rows": rows,
    "formulae": {
        "connected": (
            "C_n=(n-1)+sum_{k=4}^n s_k*binom(n-1,k-1)"
        ),
        "total": (
            "R_n=sum_{m=2}^n (n-m+1)*C_m"
        ),
        "asymptotic": "R_n/n! -> 1/e",
    },
    "regressions": [
        "Simple-permutation counts match the classical sequence through n=9.",
        "Connected counts match the independent modular classification.",
        "Total counts match direct orientation enumeration through n=7.",
        "Total counts match modular/common-interval enumeration through n=9."
    ],
    "nonclaims": [
        "The finite script does not prove the asymptotic theorem.",
        "The asymptotic proof additionally uses the classical theorem s_n/n! -> exp(-2).",
        "No claim of absolute novelty or priority is made.",
        "No physical emergence-of-time claim follows from the recovery probability."
    ],
}

print(json.dumps(result, indent=2))

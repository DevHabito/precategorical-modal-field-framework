// Prospective N=10 direct regression for random-2-order UPO recovery.
//
// This program does NOT use the substitution counting formula.
// It enumerates all 10! relative permutations and classifies them from
// comparability connected components plus the proper-common-interval
// criterion on the unique nontrivial component.
//
// Prediction frozen before execution:
//   connected UPO = 692297
//   total recoverable = 843873

#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>

static bool recoverable(
    const std::array<int, 10>& p,
    bool& connected_upo,
    std::uint64_t& internal_bad,
    std::uint64_t& multi_nontrivial,
    std::uint64_t& empty_count
) {
    constexpr int N = 10;

    std::uint16_t adjacency[N]{};
    int edge_count = 0;

    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            if (p[i] < p[j]) {
                adjacency[i] |= std::uint16_t(1u << j);
                adjacency[j] |= std::uint16_t(1u << i);
                ++edge_count;
            }
        }
    }

    if (edge_count == 0) {
        ++empty_count;
        connected_upo = false;
        return false;
    }

    bool seen[N]{};
    std::vector<std::vector<int>> components;

    for (int start = 0; start < N; ++start) {
        if (seen[start]) {
            continue;
        }

        std::vector<int> component;
        int stack[N];
        int top = 0;
        stack[top++] = start;
        seen[start] = true;

        while (top > 0) {
            int u = stack[--top];
            component.push_back(u);
            std::uint16_t neighbors = adjacency[u];

            for (int v = 0; v < N; ++v) {
                if (((neighbors >> v) & 1u) && !seen[v]) {
                    seen[v] = true;
                    stack[top++] = v;
                }
            }
        }

        components.push_back(std::move(component));
    }

    int nontrivial_index = -1;
    int nontrivial_count = 0;

    for (int c = 0; c < static_cast<int>(components.size()); ++c) {
        if (components[c].size() >= 2) {
            nontrivial_index = c;
            ++nontrivial_count;
        }
    }

    if (nontrivial_count != 1) {
        ++multi_nontrivial;
        connected_upo = false;
        return false;
    }

    auto vertices = components[nontrivial_index];
    std::sort(vertices.begin(), vertices.end());

    const int m = static_cast<int>(vertices.size());
    connected_upo = (m == N);

    int values[10];
    int sorted_values[10];
    int induced[10];

    for (int i = 0; i < m; ++i) {
        values[i] = p[vertices[i]];
        sorted_values[i] = values[i];
    }

    std::sort(sorted_values, sorted_values + m);

    for (int i = 0; i < m; ++i) {
        induced[i] = static_cast<int>(
            std::lower_bound(
                sorted_values,
                sorted_values + m,
                values[i]
            ) - sorted_values
        );
    }

    for (int left = 0; left < m; ++left) {
        int minimum = induced[left];
        int maximum = induced[left];
        bool decreasing = true;

        for (int right = left + 1; right < m; ++right) {
            if (induced[right - 1] <= induced[right]) {
                decreasing = false;
            }

            minimum = std::min(minimum, induced[right]);
            maximum = std::max(maximum, induced[right]);

            const int size = right - left + 1;

            if (
                size < m
                && maximum - minimum + 1 == size
                && !decreasing
            ) {
                ++internal_bad;
                connected_upo = false;
                return false;
            }
        }
    }

    return true;
}

int main() {
    std::array<int, 10> permutation{};
    std::iota(permutation.begin(), permutation.end(), 0);

    std::uint64_t total = 0;
    std::uint64_t recoverable_count = 0;
    std::uint64_t connected_count = 0;
    std::uint64_t internal_bad = 0;
    std::uint64_t multiple_nontrivial = 0;
    std::uint64_t empty = 0;

    do {
        ++total;

        bool connected = false;

        if (
            recoverable(
                permutation,
                connected,
                internal_bad,
                multiple_nontrivial,
                empty
            )
        ) {
            ++recoverable_count;

            if (connected) {
                ++connected_count;
            }
        }
    } while (
        std::next_permutation(
            permutation.begin(),
            permutation.end()
        )
    );

    std::cout << "total=" << total << "\n";
    std::cout << "recoverable=" << recoverable_count << "\n";
    std::cout << "connected_upo=" << connected_count << "\n";
    std::cout
        << "internal_module_ambiguity="
        << internal_bad
        << "\n";
    std::cout
        << "multiple_nontrivial_components="
        << multiple_nontrivial
        << "\n";
    std::cout << "empty_antichain=" << empty << "\n";
    std::cout
        << "partition_sum="
        << (
            recoverable_count
            + internal_bad
            + multiple_nontrivial
            + empty
        )
        << "\n";

    return 0;
}

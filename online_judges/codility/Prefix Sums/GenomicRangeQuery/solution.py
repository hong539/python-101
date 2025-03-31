# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O()
# debug
# def solution(S, P, Q):
#     S_list = list(S)
#     query_stings_impact_factor = []
#     impact_factor_dict = {"A": 1, "C":2, "G":3, "T":4}
#     result = []
#     # print(len(P))
#     # S = 'CAGCCTA'
#     # print(S[2:5])
#     for query_count in range(len(P)): #M queries
#         # print(query_count)
#         print(f"P[query_count]:{P[query_count]}, Q[query_count]:{Q[query_count]}")
#         if P[query_count] != Q[query_count]:
#             # print(S_list[P[query_count]:Q[query_count] +1 ])
#             for char in S_list[P[query_count]:Q[query_count] +1 ]:
#                 if char in impact_factor_dict.keys():
#                     query_stings_impact_factor.append(impact_factor_dict[char])
#             print(query_stings_impact_factor)
#             print(min(query_stings_impact_factor))
#             result.append(min(query_stings_impact_factor))
#             query_stings_impact_factor = []
#         elif P[query_count] == Q[query_count]:
#             print(S[P[query_count]])
#             if S[P[query_count]] in impact_factor_dict.keys():
#                 query_stings_impact_factor.append(impact_factor_dict[S[P[query_count]]])
#                 print(impact_factor_dict[S[P[query_count]]])
#             print(query_stings_impact_factor)
#             print(min(query_stings_impact_factor))
#             result.append(min(query_stings_impact_factor))
#             query_stings_impact_factor = []
#     print(result)
#     return result

# O(M × N)
# def solution(S, P, Q):
#     S_list = list(S)
#     query_stings_impact_factor = []
#     impact_factor_dict = {"A": 1, "C":2, "G":3, "T":4}
#     result = []
#     for query_count in range(len(P)): #M queries
#         if P[query_count] != Q[query_count]:
#             for char in S_list[P[query_count]:Q[query_count] +1 ]:
#                 if char in impact_factor_dict.keys():
#                     query_stings_impact_factor.append(impact_factor_dict[char])
#             result.append(min(query_stings_impact_factor))
#             query_stings_impact_factor = []
#         elif P[query_count] == Q[query_count]:
#             if S[P[query_count]] in impact_factor_dict.keys():
#                 query_stings_impact_factor.append(impact_factor_dict[S[P[query_count]]])
#             result.append(min(query_stings_impact_factor))
#             query_stings_impact_factor = []
#     return result

# O(N + M)
def solution(S, P, Q):
    """
    Given a DNA sequence S and two arrays P and Q representing M queries,
    this function returns a list of minimal impact factors in the substring S[P[i]:Q[i]+1].

    Nucleotides impact factor:
        A → 1
        C → 2
        G → 3
        T → 4 (implied if no A, C, or G in range)
    """

    N = len(S)
    M = len(P)

    # Initialize prefix sums for A, C, and G
    prefix_A = [0] * (N + 1)
    prefix_C = [0] * (N + 1)
    prefix_G = [0] * (N + 1)

    for i in range(N):
        # Copy previous value
        prefix_A[i + 1] = prefix_A[i]
        prefix_C[i + 1] = prefix_C[i]
        prefix_G[i + 1] = prefix_G[i]

        # Update if current character matches
        if S[i] == 'A':
            prefix_A[i + 1] += 1
        if S[i] == 'C':
            prefix_C[i + 1] += 1
        if S[i] == 'G':
            prefix_G[i + 1] += 1

    result = []

    for i in range(M):
        start = P[i]
        end = Q[i] + 1  # +1 because prefix sums are 1-indexed

        if prefix_A[end] - prefix_A[start] > 0:
            result.append(1)
        elif prefix_C[end] - prefix_C[start] > 0:
            result.append(2)
        elif prefix_G[end] - prefix_G[start] > 0:
            result.append(3)
        else:
            result.append(4)  # Only T remains

    return result



def main():
    print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))

if __name__ == "__main__":
    main()
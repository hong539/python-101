# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#  O(N * M)
# def solution(N, A):
#     # solution((5, [3, 4, 4, 6, 1, 4, 4]))
#     counters = [0] * N
#     for step in range(len(A)):
#         if 1 <= A[step] <= N:
#             counters[A[step] - 1] += 1
#         elif A[step] == N + 1:
#             counters = [max(counters)] * N
#     return counters

# O(N+M)
def solution(N, A):
    counters = [0] * N
    current_max = 0
    last_update = 0

    for step in range(len(A)):
        if 1 <= A[step] <= N:
            index = A[step] - 1
            if counters[index] < last_update:
                counters[index] = last_update
            counters[index] += 1
            current_max = max(current_max, counters[index])
        elif A[step] == N + 1:
            last_update = current_max

    for i in range(N):
        if counters[i] < last_update:
            counters[i] = last_update

    return counters

    

def main():
    print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
    print(solution(10, [6, 9, 7, 5, 4, 3, 2]))
    print(solution(5, [1, 2, 3, 4]))

if __name__ == "__main__":
    main()
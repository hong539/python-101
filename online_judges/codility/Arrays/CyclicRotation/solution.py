# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O(K × N)
# def solution(A, K):
#     # print("A =", A, "K =", K)
#     while K != 0:
#         K = K - 1
#         Last = A[-1]
#         # print(Last)
#         A.pop(-1)
#         # print(A)
#         A.insert(0, Last)
#     return A

# O(N)
def solution(A, K):
    N = len(A)
    if N == 0:
        return A
    K = K % N  # 若 K >= N，只需要旋轉 K mod N 次
    return A[-K:] + A[:-K]

# from collections import deque

# def solution(A, K):
#     d = deque(A)
#     d.rotate(K)
#     return list(d)

def main():
    print(solution([3, 8, 9, 7, 6], 3))
    print(solution([0, 0, 0], 1))
    print(solution([1, 2, 3, 4], 4))

if __name__ == "__main__":
    main()
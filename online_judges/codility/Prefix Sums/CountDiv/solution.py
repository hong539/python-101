# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O(B - A)
# def solution(A, B, K):
#     divisible_count = 0
#     for i in range(A, B + 1):
#         if i % K == 0:
#             divisible_count += 1
#     return divisible_count

# O(1)
def solution(A, B, K):
    return B // K - (A - 1) // K

def main():
    print(solution(6, 11, 2))
    print(solution(6, 12, 2))

if __name__ == "__main__":
    main()
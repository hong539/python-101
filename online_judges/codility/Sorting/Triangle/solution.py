# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 
# def solution(A):
#     if A[0] + A[1] > A[2]:
#         return 1
#     else:
#         return 0

# O(N log N)
def solution(A):
    A.sort()
    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1
    return 0

def main():
    print(solution([10, 2, 5, 1, 8, 20]))

if __name__ == "__main__":
    main()
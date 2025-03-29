# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O(n log n)
# def solution(A):
#     A.sort()
#     for i in range(len(A)):
#         if A[i] != i + 1:
#             return i +1
#     return len(A) + 1

# O(n)
def solution(A):
    n = len(A) + 1  # 總共應該有 n 個數字（目前缺 1 個）
    total = n * (n + 1) // 2  # 1 到 n 的總和
    return total - sum(A)     # 總和 - 現有的和 = 缺的數字

def main():    
    print(solution([2,3,1,5]))
    print(solution([1,6,5,3,4]))

if __name__ == "__main__":
    main()
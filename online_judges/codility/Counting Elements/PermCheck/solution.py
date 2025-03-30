# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# performance
# def solution(A):
#     # solution([4, 1, 3, 2])
#     B = set(range(1, len(A)+1))
#     A_set = set(A)
#     print(B)
#     if A_set == B:
#         return 1
#     else:
#         return 0
    
# set + max/min法
def solution(A):
    A_set = set(A)
    if len(A_set) != len(A):
        return 0  # 有重複值，不是排列
    if max(A_set) != len(A) or min(A_set) != 1:
        return 0  # 最小值不是1，最大值不是N，不是排列
    return 1

#
# def solution(A):
#     N = len(A)
#     seen = [False] * N
#     for num in A:
#         if num < 1 or num > N:
#             return 0
#         if seen[num - 1]:
#             return 0
#         seen[num - 1] = True
#     return 1
    

def main():
    print(solution([4, 1, 3, 2]))
    print(solution([4, 1, 3]))

if __name__ == "__main__":
    main()
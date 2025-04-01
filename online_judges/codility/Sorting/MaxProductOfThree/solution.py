# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# # O(N log N)
# def solution(A):
#     top3 = sorted(A, reverse=True)[:3]
#     return top3[0] * top3[1] * top3[2]

# # O(N log N)
# def solution(A):
#     A.sort()
#     # 三個最大的正數
#     # 兩個最小的負數 + 最大的正數
#     return max(A[-1] * A[-2] * A[-3], A[0] * A[1] * A[-1])

# O(N)
def solution(A):
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for num in A:
        # 找最大三個
        if num > max1:
            max1, max2, max3 = num, max1, max2
        elif num > max2:
            max2, max3 = num, max2
        elif num > max3:
            max3 = num
        
        # 找最小兩個
        if num < min1:
            min1, min2 = num, min1
        elif num < min2:
            min2 = num

    return max(max1 * max2 * max3, min1 * min2 * max1)

def main():
    print(solution([-3, 1, 2, -2, 5, 6]))

if __name__ == "__main__":
    main()
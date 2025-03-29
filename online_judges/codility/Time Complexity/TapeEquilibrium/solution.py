# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O(N^2)
# def solution(A):
#     N = len(A)
#     difference_list = []
#     for P in range(N):        
#         left = A[:P]
#         right = A[P:]
#         difference = abs(sum(left) - sum(right))
#         difference_list.append(difference)
#     return min(difference_list)

# O(n)
def solution(A):
    total = sum(A)  # 總和只算一次
    left_sum = 0
    min_diff = float('inf')

    for P in range(1, len(A)):  # 注意：從 P=1 開始，避免空陣列
        left_sum += A[P - 1]
        right_sum = total - left_sum
        diff = abs(left_sum - right_sum)
        min_diff = min(min_diff, diff)

    return min_diff


def main():    
    print(solution([3,1,2,4,3]))
    print(solution([1,6,5,3,4]))

if __name__ == "__main__":
    main()
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 
# def solution(A):
#     # slice len = 2
#     # slice (1, 2), whose average is (2 + 2) / 2 = 2;
#     # slice (3, 4), whose average is (5 + 1) / 2 = 3;
#     # slice len = 3
#     # slice len = 4
#     # slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
#     # slice len = 5
#     # slice len = 6
#     # slice len = 7
#     # slice_avg = 0
#     avg = sum(A) / len(A)
#     # for i in range(len(A)):
#     #     slice_avg = sum(A[i:i+1]) / len(A[i:i+1])

#     return avg

# O(N)
def solution(A):
    min_avg = float('inf')  # 初始最小平均
    min_index = 0  # 初始位置

    for i in range(len(A) - 1):
        # 長度為 2 的 slice
        avg2 = (A[i] + A[i + 1]) / 2
        if avg2 < min_avg:
            min_avg = avg2
            min_index = i

        # 長度為 3 的 slice（如果有的話）
        if i + 2 < len(A):
            avg3 = (A[i] + A[i + 1] + A[i + 2]) / 3
            if avg3 < min_avg:
                min_avg = avg3
                min_index = i

    return min_index



def main():
    print(solution([4, 2, 2, 5, 1, 5, 8]))

if __name__ == "__main__":
    main()
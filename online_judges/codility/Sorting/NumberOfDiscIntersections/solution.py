# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O(N^2)
# def solution(A):
#     N = len(A)
#     count = 0
#     for i in range(N):
#         for j in range(i + 1, N):
#             if (i - A[i]) <= (j + A[j]) and (j - A[j]) <= (i + A[i]):
#                 count += 1
#     return count


# O(N log N)
def solution(A):
    N = len(A)
    left = [i - A[i] for i in range(N)]
    right = [i + A[i] for i in range(N)]

    left.sort()
    right.sort()

    intersections = 0
    j = 0
    for i in range(N):
        while j < N and right[i] >= left[j]:
            j += 1
        intersections += j - i - 1
        if intersections > 10_000_000:
            return -1
    return intersections

def main():
    print(solution([1, 5, 2, 1, 4, 0]))

if __name__ == "__main__":
    main()
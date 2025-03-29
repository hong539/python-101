# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O(N²)
# O(N)（外層 for） × O(N)（count） = O(N²)
# def solution(A):
#     for x in A:
#         if (A.count(x) % 2) != 0:
#             return x

# O(N)
from collections import Counter
def solution(A):
    count = Counter(A)
    for k in count:
        if count[k] % 2 == 1:
            return k

# XOR 位元運算
def solution(A):
    result = 0
    for x in A:
        result = result ^ x
    return result


def main():
    # print(solution([1, 3, 5, 7, 9, 1]))
    print(solution([9, 3, 9, 3, 9, 7, 9]))

if __name__ == "__main__":
    main()
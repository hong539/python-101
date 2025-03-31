# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O(n^2)
def solution(A):    
    B = list(range(1, len(A) +2 ))
    for x in B:
        if x not in A:
            return x


# O(n)
# def solution(A):
#     set_A = set(A)    
#     for i in range(1, len(A) + 2):
#         if i not in set_A:
#             return i

def main():
    print(solution([1, 3, 6, 4, 1, 2]))
    print(solution([1, 2, 3, 4, 5]))
    print(solution([1, 2, 3]))
    print(solution([-1, -3]))

if __name__ == "__main__":
    main()
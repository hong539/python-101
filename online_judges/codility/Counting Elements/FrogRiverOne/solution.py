# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# UnboundLocalError: local variable 'K' referenced before assignment
# def solution(X, A):
#     # solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
#     B = list(range(1,X+1))
#     for i in range(len(A)):
#         while A[i] not in B:
#             K = i
#     return K

# O(1)
def solution(X, A):
    B = set(range(1, X + 1))
    covered = set()
    for i in range(len(A)):
        if A[i] in B:
            covered.add(A[i])
            if covered == B:
                return i
    return -1

def main():
    print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

if __name__ == "__main__":
    main()
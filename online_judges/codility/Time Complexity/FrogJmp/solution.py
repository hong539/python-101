# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O((Y - X) / D)
# TLE（Time Limit Exceeded）
# def solution(X, Y, D):
#     jumps = 0
#     pos = X
#     while pos <= Y:
#         jumps = jumps + 1
#         pos = pos + D
#     return jumps


# O(1)
def solution(X, Y, D):
    return (Y - X + D - 1) // D

# O(1)
# import math
# def solution(X, Y, D):
#     return math.ceil((Y - X) / D)

def main():    
    print(solution(10, 85, 30))
    print(solution(10, 1000000000, 30))

if __name__ == "__main__":
    main()
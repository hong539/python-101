# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O(K × N)
# def solution(N):
#     enable_print = N % 10
#     while N > 0:
#         if enable_print == 0 and N % 10 != 0:
#             enable_print = 1
#         elif enable_print == 1:
#             print(N % 10, end="")
#         N = N // 10

# modify
def solution(N):
    enable_print = 0
    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
            print(N % 10, end="")
        elif enable_print == 1:
            print(N % 10, end="")
        N = N // 10

def main():
    # print(solution(54321))
    # print(solution(10011))
    # print(solution(1))
    solution(10010)
    # solution(1000)

if __name__ == "__main__":
    main()
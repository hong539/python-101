# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# def solution(A):
#     income = 0
#     for i in range(1, len(A)):
#         if A[i] > A[i - 1]:
#             income += A[i] - A[i-1]
#     result = income % 1_000_000_000
#     return result

def solution(A):
    income = 0
    holding = True  # 一開始持有
    buy_price = A[0]

    for i in range(1, len(A)):
        if holding and A[i] < A[i - 1]:
            # 即將下跌：賣出
            income += A[i - 1]
            holding = False
        elif not holding and A[i] > A[i - 1]:
            # 即將上升：買進
            buy_price = A[i - 1]
            income -= buy_price
            holding = True

    # 如果最後一天還在持有，要賣掉
    if holding:
        income += A[-1]

    return income % 1_000_000_000


def main():
    print(solution([4, 1, 2, 3]))
    # solution([5, 1, 6, 8, 8, 8])
    print(solution([1, 2, 3, 3, 2, 1, 5]))
    print(solution([1000000000, 1, 2, 2, 1000000000, 1, 1000000000]))
    

if __name__ == "__main__":
    main()
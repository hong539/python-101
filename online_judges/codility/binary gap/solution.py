# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    return len(max(format(N,'b').strip('0').split('1')))

def main():
    print(solution(9))
    print(solution(529))
    print(solution(20))
    print(solution(15))
    print(solution(32))

if __name__ == "__main__":
    main()
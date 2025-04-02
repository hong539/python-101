# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# O(N)
def solution(A):    
    return len(set(A))

def main():
    print(solution([2, 1, 1, 2, 3, 1]))
    print(solution([1, 6 , 9, 6, 9, 3 ,10]))

if __name__ == "__main__":
    main()
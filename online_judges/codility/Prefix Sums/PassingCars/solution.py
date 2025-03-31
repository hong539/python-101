# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 
def solution(A):
    east = A.count(0)
    west = A.count(1)
    total_pairs = east * west

    east_seen = 0
    invalid_pairs = 0

    for x in A:
        if x == 0:
            east_seen += 1
        elif x == 1:
            invalid_pairs += (east - east_seen)

    result = total_pairs - invalid_pairs
    return -1 if result > 1_000_000_000 else result

#
# def solution(A):
#     east_cars = 0
#     passing_pairs = 0
    
#     for car in A:
#         if car == 0:
#             east_cars += 1
#         else:  # car == 1
#             passing_pairs += east_cars
#             if passing_pairs > 1_000_000_000:
#                 return -1
    
#     return passing_pairs


def main():
    print(solution([0, 1, 0, 1, 1]))
    print(solution([1, 0, 1, 0, 0]))
    print(solution([0, 1, 1]))

if __name__ == "__main__":
    main()
# 114114390	A Python 3.12.1
def min_platforms_for_robots(robots_weight: list, plate_limit: int) -> int:
    """
    Determine the minimum number of transportation platforms
    required to transport all robots described in the array.
    """

    robots_weight: list = sorted(robots_weight)

    plate_count: int = 0
    left_ptr: int = 0
    right_ptr: int = len(robots_weight) - 1

    while left_ptr <= right_ptr:
        if robots_weight[left_ptr] + robots_weight[right_ptr] <= plate_limit:
            left_ptr += 1
        right_ptr -= 1
        plate_count += 1

    return plate_count


if __name__ == '__main__':
    test_case_list: list = [int(num) for num in input().split()]
    test_case_limit: int = int(input())
    print(min_platforms_for_robots(test_case_list, test_case_limit))

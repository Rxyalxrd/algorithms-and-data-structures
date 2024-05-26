import sys


def exist_num_in_list(list_of_nums, element):
    return element in list_of_nums


def binary_search_index(list_of_nums, element):

    if not exist_num_in_list(list_of_nums, element):
        list_of_nums.append(element)
        list_of_nums.sort()

    left_ptr = 0
    right_ptr = len(list_of_nums) - 1

    while left_ptr <= right_ptr:
        mid = (left_ptr + right_ptr) // 2
        if list_of_nums[mid] == element:
            while mid > 0 and list_of_nums[mid - 1] == element:
                mid -= 1
            return mid
        elif list_of_nums[mid] < element:
            left_ptr = mid + 1
        else:
            right_ptr = mid - 1


def main():
    list_of_nums = list(map(int, sys.stdin.readline().rstrip().split()))
    target = int(sys.stdin.readline().rstrip())
    result = binary_search_index(list_of_nums, target)
    print(result)


if __name__ == '__main__':
    main()

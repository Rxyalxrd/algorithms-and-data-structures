import sys


def count_smaller_elements(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result


def main():
    nums = [int(num) for num in sys.stdin.readline().rstrip().split()]
    print(*count_smaller_elements(nums))


if __name__ == '__main__':
    main()

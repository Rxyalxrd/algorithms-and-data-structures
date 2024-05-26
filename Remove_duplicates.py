import sys


def delete_duplicates(length, nums):
    res = []

    for num in nums:
        if num not in res:
            res.append(num)

    res.sort()

    while len(res) != length:
        res.append('_')

    res = list(map(str, res))

    return res


def main():
    length = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    result = delete_duplicates(length, nums)
    print(' '.join(result))


if __name__ == '__main__':
    main()

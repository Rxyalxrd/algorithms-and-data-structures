import sys


def longest_substring_length(s):
    if not s:
        return 0

    max_length = 0
    start = 0
    seen = {}

    for end, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length


def main():
    test_case = sys.stdin.readline().rstrip()
    print(longest_substring_length(test_case))


if __name__ == '__main__':
    main()

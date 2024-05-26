import sys


def fibonacci_solution(num: int) -> int:
    if num == 0 or num == 1:
        return 1

    return fibonacci_solution(num - 1) + fibonacci_solution(num - 2)


if __name__ == '__main__':
    test_case: int = int(sys.stdin.readline().rstrip())
    print(fibonacci_solution(test_case))

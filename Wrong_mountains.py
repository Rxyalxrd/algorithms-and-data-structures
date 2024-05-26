import sys
from array import array


def valid_mountain_array(lst: array) -> bool:

    peak: int = max(lst)
    peak_index: int = lst.index(peak)
    value: int = 0
    flag: bool = True

    if len(lst) < 3:
        return not flag

    if peak_index == len(lst) - 1 or peak_index == 0:
        return not flag

    while value < peak_index:
        if lst[value] < lst[value + 1]:
            value += 1
        else:
            flag = False
            break

    while peak_index < len(lst) - 1:
        if lst[peak_index] > lst[peak_index + 1]:
            peak_index += 1
        else:
            flag = False
            break

    return flag


def main():
    array_input = sys.stdin.readline().rstrip().split()
    test_case = array('h', [int(num) for num in array_input])
    try:
        print(valid_mountain_array(test_case))
    except Exception:
        print('Unexpected behavior')


if __name__ == '__main__':
    main()

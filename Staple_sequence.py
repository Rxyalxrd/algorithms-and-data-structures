import sys


class Stack:
    def __init__(self):
        self.__my_list = []

    def push(self, item):
        self.__my_list.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__my_list.pop()
        else:
            return None

    def is_empty(self):
        return len(self.__my_list) == 0

    def peek(self):
        if not self.is_empty():
            return self.__my_list[-1]
        else:
            return None


def main():
    stack = Stack()
    target_value = {')': '(', '}': '{', ']': '['}
    test_case = [char for char in sys.stdin.readline().rstrip()]

    for char in test_case:
        if char in target_value.values():
            stack.push(char)
        elif char in target_value.keys():
            if stack.is_empty() or target_value[char] != stack.pop():
                return False
        else:
            return False

    print(stack.is_empty())


if __name__ == '__main__':
    main()

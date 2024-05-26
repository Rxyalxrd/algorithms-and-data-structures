def solution(count_num_in_list, list_of_num, len_res_list, template_list):
    count_num = {}

    for num in list_of_num:
        if num in count_num:
            count_num[num] += 1
        else:
            count_num[num] = 1

    result = []

    for num in template_list:
        if num in count_num:
            result.extend([num] * count_num[num])
            del count_num[num]

    remaining = sorted(
        [num for num in count_num for _ in range(count_num[num])]
    )
    result.extend(remaining)

    return result


def main():
    count_num_in_list = int(input())
    list_of_num = [int(item) for item in input().split()]
    len_res_list = int(input())
    template_list = [int(item) for item in input().split()]
    print(*solution(
        count_num_in_list, list_of_num, len_res_list, template_list
        )
    )


if __name__ == '__main__':
    main()

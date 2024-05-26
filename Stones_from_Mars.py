def solution(orders, orders_list, samples, samples_list):
    count = 0

    orders_list.sort()
    samples_list.sort()

    len_samples = len(samples_list)
    len_orders = len(orders_list)

    ptr_order = 0
    ptr_sample = 0

    while ptr_order < len_orders and ptr_sample < len_samples:
        if orders_list[ptr_order] <= samples_list[ptr_sample]:
            count += 1
            ptr_order += 1
        ptr_sample += 1

    return count


orders = int(input())
orders_list = list(map(int, input().split()))
samples = int(input())
samples_list = list(map(int, input().split()))
print(solution(orders, orders_list, samples, samples_list))

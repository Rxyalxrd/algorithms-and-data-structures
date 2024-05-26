def max_blocks_to_sort(n, arr):
    blocks = 0
    max_in_block = 0

    for i in range(n):
        max_in_block = max(max_in_block, arr[i])
        if max_in_block == i:
            blocks += 1

    return blocks


n = int(input())
arr = list(map(int, input().split()))

print(max_blocks_to_sort(n, arr))

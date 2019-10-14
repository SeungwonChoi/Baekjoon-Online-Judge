# https://www.acmicpc.net/problem/11047

type_num, target_value = map(int, input().split())
values = [0] * type_num
max_idx = type_num - 1

for i in range(type_num):
    values[i] = int(input())
    if values[i] > target_value:
        max_idx = i - 1
        break
cnt = 0

for i in range(max_idx, -1, -1):
    cnt += target_value // values[i]
    target_value = target_value % values[i]
print(cnt)

# https://www.acmicpc.net/problem/11399

user_num = int(input())
times = sorted(list(map(int, input().split())))
print(sum(times[i] * (len(times) - i) for i in range(0, len(times))))

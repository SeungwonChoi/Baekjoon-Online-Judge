# https://www.acmicpc.net/problem/2588

num_1 = int(input())
num_2_str = input()
for i in num_2_str[::-1]:
    print(num_1 * int(i))
print(num_1 * int(num_2_str))

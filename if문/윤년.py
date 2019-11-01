# https://www.acmicpc.net/problem/2753

year = int(input())
print(1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 0)

# https://www.acmicpc.net/problem/1330

A, B = map(int, input().split())
print("<" if A < B else (">" if A > B else "=="))

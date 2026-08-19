# 입출력 처리

# 1개 입력
# a = input()
# print(a)
# print(type(a))
# a = input()  # --a = int(input())
# a = int(a)  # ---^
# print(type(a))
# b = float(input())
# print(b, type(b))
# m = int(input())
# n = int(input())
# print(m, n)
# a = input().split()
# print(a)
# map(함수, 리스트)
a, b, c = map(int, input().split())
print(a, b, c)

l = list(map(int, input().split()))
print(l)

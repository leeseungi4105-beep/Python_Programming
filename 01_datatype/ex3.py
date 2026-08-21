# 불리언
# True or False
a = True
print(a, type(a))
print(1 > 0)
print(1 < 0)
print(1 == 0)
print(1 != 0)

print("apple" > "apble")

print(bool(3))
print(bool(0))
print(bool("hey"))
print(bool(""))

print(bool([1]))
print(bool([]))

# None 자료형
a = None  # 비교할 때 isNone
print(a, type(a))
print(bool(a))

if a is None:
    print("값이 없음")

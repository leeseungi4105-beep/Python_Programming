# 문자열
# "" ''

a = "python"
print(a, type(a))

print("I'll be back")
print("I'll be back")
multiline = """
Life is short
You need python
"""
print(multiline)


# docstring """ """
def func():
    """테스트 전용"""
    pass


print(func.__doc__)
print("Hello" + " Python")  # LMAO

# 문자열 반복
print("Hello" * 10)

# print("Hello" + 10)  X
print("Hello" + str(10))
print(int("10") + int("2"))
print(eval("10" + "2"))  # 되나

name = "pororo"
age = 23
print(f"이름: {name}, 나이: {age}세")
print(f"내년 나이: {age + 1}세")
print(f"{name.upper()}")

pi = 3.1415926535897932384626433832795028841971693
print(f"{pi:.3f}")
print(f"{pi:.0f}")
num = 123456789
print(f"{num:,}")
print(f"{num:15d}")
print(f"{num:<15d}")
print(f"{num:015d}")
print(f"{num:015,d}")

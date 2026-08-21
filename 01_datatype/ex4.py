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
print(eval("10" + "2"))

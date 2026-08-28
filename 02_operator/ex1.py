# 연산자

# 산술 연산자
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)  # 나머지
print(a // b)  # 몫
print(a**b)

# 복합대입연산자
a = 0
a += 4
print(a)
# a++ (X)
a -= 2
print(a)

# 비교 연산자
print(3 == 3.0)
print(3 != 4)
print("apple" < "apble")
print(1 < 3 < 2)  # 1<2 and 2<3
print(1 < 3 < 2)

# 논리연산자(and, or, not)
a = True
b = False

print(a and b)  # &&
print(a or b)  # ||
print(not b)

# Short-circuit
a = 10
b = 0

# print(a / b)

if a > 0 or a / b:
    print("yes")
else:
    print("no")

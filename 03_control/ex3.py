# for문
# for i in range iterable객체:
# ...
for i in range(5):
    print(i, "End")  # 0!4

a = range(5)
print(
    a.start,
    a.stop,
)
# 5~1
for i in range(1, 10, 2):
    print(i, end=" ")
for i in range(5, 0, -1):
    print(i)

tot = 0
for i in range(1, 10):
    tot += i
    i += 1
print(tot)

print(sum(range(1, 11)))

s = "ehioaㅇㄴㅁ랴ㅓ❓ㅗ"

for c in s:
    print(c, end=" ")

print(len(s))

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j:<5d}", end="")
        j += 1
    i += 1

from random import randint

print('what do you want')
n = int(input())
num1 = 3
a = 0
b = 0

while b <= n:
    num2 = randint(1, 3)
    b = b+1
    if num1 == num2:
        a = a+1
ans = a/n
print('%f' % ans)


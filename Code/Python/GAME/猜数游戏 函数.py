from random import randint


def end(num1, num2):
    if num1 > num2:
        print("%d is too big" % ans)
        return False
    elif num1 < num2:
        print("%d is too small" % ans)
        return False
    else:
        print("%d is the right answer" % ans)
        return True


print("Guess what I am thinking")
bro = False
num = randint(1, 100)
while bro is False:
    ans = int(input())
    bro = end(ans, num)

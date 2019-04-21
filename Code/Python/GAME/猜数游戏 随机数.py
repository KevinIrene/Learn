from random import randint
num = randint(1, 100)

print("Guess What I am thinking")
you = False

while you is False:
    ans = int(input())
    if ans < num:
        print("%d is Too small" % ans)
    if ans > num:
        print("%d is Too big" % ans)
    if ans == num:
        print('bingo %d is the right answer' % ans)
        you = True
        break
    break

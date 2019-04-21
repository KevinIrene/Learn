num = 10
print("Guess What I am thinking")
you = False

while True:
    answer = int(input())

    if answer > num:
        print("%d is too big" % answer)
    if answer < num:
        print("%d is too small" % answer)
    if answer == num:
        print("Bingo %d is the right answer" % answer, end='  ')
        print("You are so clever")
        break

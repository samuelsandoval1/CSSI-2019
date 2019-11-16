import random


def roll_dice(num):
    # random_num = random.randint(1,6)
    sum = 0
    for number in range(0, num):
        random_num = random.randint(1,6)
        sum = sum + random_num
        print "Roll " + str(number+1) + " equals: " + str(random_num)
    return sum
print(roll_dice(4))

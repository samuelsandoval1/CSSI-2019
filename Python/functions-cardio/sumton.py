#example 3

def sum_to_n(num):
    sum = 0
    for number in range(0, num + 1):
        sum += number
    return sum

print(sum_to_n(4))

# HW 8.14

# CS255


def squaring(num):

    sum = 0

    if (num < 0):
        return 0

    if (num == 1):
        return 1

    for x in range(0, num):
        for y in range(0, num):
            sum += 1
    return sum + squaring(num-1)

print squaring(5)

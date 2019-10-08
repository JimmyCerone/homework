# HW 8.14

# CS255

sum = 0

def squaring(num):
    global sum
    for x in range(0, num):
        for y in range(0, num):
            sum += 1
    return sum

print squaring(5)

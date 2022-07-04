#logical operators
#....................

# AND  &
# OR    |
# XOR    ^

#AND operator

num1=2
num2=4
print(num1&num2)

num1=6
num2=4
print(num1&num2)

num1=4
num2=4
print(num1&num2)

num1=3
num2=4
print(num1&num2)

# 0 0 0
# 1 0 0
# 0 1 0
# 1 1 1

#0010 & 0100  -0
#0100 & 0100 -0100
#0110 & 0100 -0100
#0011 & 0100 - 0000

#OR operator

# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 1

num1=5
num2=3
print(num1|num2)

#0101 | 0011 - 0111-7

#XOR

# 0 0 0
# 0 1 1
# 1 0 1
# 1 1 0

#0110 ^ 0111 = 0001


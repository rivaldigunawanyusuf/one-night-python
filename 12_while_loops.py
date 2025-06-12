# 12 - While Loops

# Basic while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # increment to avoid infinite loop

# Using break to exit the loop
n = 0
while True:
    print("n =", n)
    n += 1
    if n == 3:
        break  # loop ends when n equals 3

# Using continue to skip an iteration
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue  # skip this iteration
    print("x =", x)

# Infinite loop (be careful)
# while True:
#     print("This runs forever.")  # uncomment with caution

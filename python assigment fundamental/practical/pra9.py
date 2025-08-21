import math
num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    prime = True

    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

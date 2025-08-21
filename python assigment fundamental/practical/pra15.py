def generate_even_numbers():
    num = 0
    count = 0
    while count < 10:
        yield num
        num += 2
        count += 1

for even in generate_even_numbers():
    print(even)

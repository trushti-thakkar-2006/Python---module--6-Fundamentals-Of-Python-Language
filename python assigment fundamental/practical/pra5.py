import math 

PI = 3.14
def calculate_area(radius):
    return PI * (radius ** 2)


def greet_user(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    user_name = "trushti"
    circle_radius = 5

    greet_user(user_name)
    area = calculate_area(circle_radius)

    print(f"The area of a circle with radius {circle_radius} is {area:.2f}")

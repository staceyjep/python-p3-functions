#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    print(f"Hello, {name}!")
greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
greet_with_default()
greet_with_default("Sunny")

def add(num1, num2):
    return num1 + num2
sum_of_numbers= add(1,2)
print(sum_of_numbers)


def halve(number):
    if not isinstance(number, (int, float)):
        return None  # Returns None if the number is not an int or float
    return number / 2

result1 = halve(4)
print(result1)  

result2 = halve("two")
print(result2)  

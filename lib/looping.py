#!/usr/bin/env python3

def happy_new_year():
    for i in range(10,0,-1):
        print(i)
        if i == 1:
            print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    return [i ** 2 for i in int_list]



def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Example usage:
for i in range(1, 101):  # Test it for numbers from 1 to 100
    fizzbuzz(i)


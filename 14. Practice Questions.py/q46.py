"""
Q.46
write a function fizzbuzz(n) that takes a single number and prints "Fizz" if it's divisible by 3, "Buzz" if it's divisible by both, otherwise print the number itself.

"""
def fizzbuzz(n):
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%5==0:
        print("Buzz")
    elif n%3==0:
        print("Fizz")
    else:
        print(n)

fizzbuzz(9)
fizzbuzz(20)
fizzbuzz(15)
fizzbuzz(7)
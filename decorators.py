#decorators in python:-
def greet(fx):
    def mfx():
        print("Good Morning Sir💖")
        fx()
        print("Thanks for using this function✌️")
    return mfx






@greet
def hello():
    print("hello world")
    hello()    



# use mfx(self) and fx(self) as argument to run this code
# When using a decorator on a class method,
# the wrapper function inside the decorator must accept self as an argument —
def greet(fx):
    def mfx(self):
        print("Good Morning Sir💖")
        fx(self)
        print("Thanks for using this function✌️")
    return mfx

class Person:
    name="Harry"
    occ="Devloper"
    @greet
    def info(self):
        print(f"{self.name} is a {self.occ}.")

a=Person()
a.info()      


def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning Sir💖")
        fx(*args, **kwargs)
        print("Thanks for using this function✌️")
    return mfx

def add(*args):
    print(sum(args))
greet(add)(1,2,3,4,5,6)    



def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning Sir💖")
        fx(*args, **kwargs)
        print("Thanks for using this function✌️")
    return mfx

@greet
def add(a,b):
    print(a+b)
add(1,2)    


def happy(fx):
    def mfx(*args, **kwargs):
        print("oh! let's use this function bro'😁📩")
        fx(*args, **kwargs)
        print("The required output is just above check it!😊🔪")
    return mfx


@happy
def average(a,b):
        print((a+b)/2)
average(5,7)    

import math
def welcome(fx):
    def mfx(*args, **kwargs):
        print("Welcome to my function")
        fx(*args, **kwargs)
        print(" Thankyou! Use again.❤️")
    return mfx

@welcome
def mul(*args):
    print(math.prod(args))
mul(2,5,5,2)


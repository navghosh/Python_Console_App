#Building a calculator

from math import *
print(f"Hello User, ")


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x / y


def mod(x, y):
    return x%y


def sqrt(x):
    return x**0.5


def cube_root(x):
    return x**(1/3)


def pow(x,y):
    return x**y

print("Choose Option (1/2/3/4/5/6/7/8) ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Square root")
print("7. Cube root")
print("8. Power")


Choice = input(f"select from options: ")

if Choice == "1":
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))
    print(x,'+', y,'=', add(x,y))

elif Choice == "2":
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))
    print(x,'-', y,'=', sub(x,y))

elif Choice == "3":
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))
    print(x,'*', y,'=', mul(x,y))

elif Choice == "4":
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))
    if y==0:
        print(f'zero division not possible, try valid input')
    else:
        print(x,'/', y,'=', div(x,y))

elif Choice == "5":
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))
    print(x,'%', y,'=', mod(x,y))

elif Choice == "6":
    x = int(input('enter number: '))
    print(x,'**', 0.5,'=', sqrt(x))

elif Choice == "7":
    x = int(input('enter number: '))
    print(x,'**', (1/3),'=', cube_root(x))

elif Choice == "8":
    x = int(input('enter first number: '))
    y = int(input('enter second number: '))
    print(x,'**', y,'=', pow(x,y))

else:
    print(f"it's a invalid input, choose from options")

print("ThankYou!!")
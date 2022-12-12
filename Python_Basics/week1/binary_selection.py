#conditional excution
#1. binary selection:
x = input("Enter a number ?")
x = int(x)  # convert the value to int
if x % 2 == 0:
    print(x, 'is even')
else :
    print(x, 'is odd')
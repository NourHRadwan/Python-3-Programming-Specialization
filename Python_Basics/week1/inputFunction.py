#Python input() function is used to take user input. By default, 
# it returns the user input in form of a string.
#example 1 arithmatic
num1 = input('please enter the 1st number ')
num2 = input('please enter the 2nd number ')
print(type(num1))
addition = int(num1) + int(num2)
print('the numbers are {} and {}'.format(num1 , num2))
print('The sum of two number is {}'.format(addition))

#example 2 concatenation 
str1 = input('enter your first name ')
str2 = input('enter your 2nd name ')
print('hello '+ str1 + ' '+ str2)

#DataType Casting
#? Input from the terminal is always a string. So, we need to cast it to the required data type.
number1 = input("enter a number: ") #? this will take input from the user and store it in number1 as a string
print(type(number1)) #? this will print the data type of number1

number2 = float(input("enter another number: ")) #? this will take input from the user, cast it to a float and store it in number2
print(type(number2)) #?

print(number1 + number2)

#convert string into float
number1 = float(number1)
number2 = float(number2)
print(type(number1), type(number2))

print(number1 + number2)
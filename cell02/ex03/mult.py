#!/usr/bin/env python3
type_number1 = int(input("Enter the first number: "))
type_number2 = int(input("Enter the second number:"))

result = type_number1 * type_number2
print(type_number1,"x",type_number2,"=",result)

if result < 0:
    print ("This result is negative.")
elif result == 0:
    print ("This result is both positive and negative.")
else:
    print ("This result is positive.")
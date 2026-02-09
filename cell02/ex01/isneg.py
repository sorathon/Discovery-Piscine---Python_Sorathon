#!/usr/bin/env python3

type_number = int(input("Enter a number: "))

if type_number < 0:
    print ("This number is negative.")
elif type_number == 0:
    print ("This number is both positive and negative.")
else:
    print ("This number is positive.")
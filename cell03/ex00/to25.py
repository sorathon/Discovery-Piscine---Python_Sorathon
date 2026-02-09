#!/usr/bin/env python3

user = int(input("Enter a number less than 25 : "))

if user > 25 :
    print("Error")
else :
    while user <= 25 :
        print("Inside the loop, my variable is " , user)
        user += 1
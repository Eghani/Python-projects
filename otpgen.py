# otp generator in pyhton 


import random

# making a function for better understanding
def otp_gen(lenght = 6):
    otp = ''
    # you can chose the lenght of the otp 4 / 6 
    for _ in range(lenght):
        otp += str(random.randint(0,9))
    return otp

otp = otp_gen()
print(f"Your OTP is : {otp}")



"""

OTP Generator in Python

The code provided is a Python script for generating a One-Time Password (OTP). Here’s a breakdown of how it works:

Importing the Random Module

The script begins by importing the random module. This module contains functions for generating random numbers.
Defining the OTP Generation Function

The function otp_gen is defined with a parameter length that defaults to 6. This parameter allows the user to specify the desired length of the OTP.
Inside the function, an empty string otp is initialized to store the generated OTP.
Generating the OTP

A for loop runs for the number of times specified by the length parameter.
During each iteration of the loop, a random integer between 0 and 9 is generated using random.randint(0, 9).
The generated random number is converted to a string and concatenated to the otp string.
Returning the OTP

After the loop completes, the function returns the generated OTP as a string.

Generating and Printing the OTP

The otp_gen function is called without any arguments, so it uses the default length of 6.
The generated OTP is stored in the variable otp.
Finally, the OTP is printed to the console using an f-string for formatting.
This script provides a simple way to generate a numerical OTP of a specified length, with a default length of 6 digits.

"""
#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: May, 4, 2022
# This program asks the user for the tempreture in
# in celsius and then we convert it to fahrenheit using
# function.


# declaring funtion
def fahrenheit():

    # ask users for temperature in celsius
    temperature_c = input("Enter the temperature in Celsius: ")
    print("")

    # check for type of input
    try:
        float_temperature = float(temperature_c)
        print("")
        celcius_to_fahrenheit = float_temperature * 1.8 + 32
        print("The temperature in Fahrenheit is {:.1f}° "
              .format(celcius_to_fahrenheit))

    # check for type of input
    except Exception:
        print("")
        print("Invalid input. Input was not a number..")


def main():
    # calling the function
    fahrenheit()


if __name__ == "__main__":
    main()


#Write a program to convert temperature in Celsius to Fahrenheit using map function
#Write the above program using lambda expression.
celsius_temps = [0, 20, 37, 100, -10]
fahrenheit_temps = list(map(lambda c: (c * 9 / 5) + 32, celsius_temps))
print("Celsius:", celsius_temps)
print("Fahrenheit:", fahrenheit_temps)
#Write a program to convert temperature in Celsius to Fahrenheit using map function.
def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32
celsius_temps=[0,34,87]
fahrenheit_temps=list(map(celsius_to_fahrenheit,celsius_temps))
print("Celcius:",celsius_temps)
print("Fahrenheit:",fahrenheit_temps)



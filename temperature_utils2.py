import unittest
import temperature_utils

def convert_to_kelvin(celsius_temp: float) -> float:
    kelvin = celsius_temp + 273.15
    print(str(celsius_temp) + " degrees celsius is equal to " + str(float(kelvin)) + " degrees kelvin.")
    return kelvin


# def convert_to_fahrenheit(celsius_temp: float) -> int:
#     fahrenheit = (celsius_temp * 9 / 5) + 32
#     print(str(celsius_temp) + "degrees celsius is equal to " + str(int(fahrenheit)) + " degrees fahrenheit.")
#     return round(fahrenheit, 2)
# pass
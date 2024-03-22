from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    celsius = (fahrenheit_temp - 32) * 5 / 9
    print(str(fahrenheit_temp) + "degrees fahrenheit is equal to " + str(int(celsius)) + " degrees celsius.")
    return round(celsius, 2)

"""
Given a float representing a temperature in Fahrenheit, return the corresponding value in Celsius.

:param Fahrenheit_temp: A float representing a temperature in Fahrenheit
:return: A float representing the corresponding value of the Fahrenheit_temp parameter in Celsius
"""

def convert_to_fahrenheit(celsius_temp: float) -> int:
    fahrenheit = (celsius_temp * 9 / 5) + 32
    print(str(celsius_temp) + "degrees celsius is equal to " + str(int(fahrenheit)) + " degrees fahrenheit.")
    return round(fahrenheit, 2)


"""
Given a float representing a temperature in Celsius, return the corresponding value in Fahrenheit.

:param Celsius_temp: A float representing a temperature in Celsius
:return:  A float representing the corresponding value of the Celsius_temp parameter in Fahrenheit
"""


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:

    tupleOftuples = ()

    for temp in temperatures:
        if input_unit_of_measurement == "c":
            f = (temp * 9 / 5) + 32
            tupleOftuples += (float(temp), round(f, 2)),

        elif input_unit_of_measurement == "f":
            c = (temp - 32) * 5 / 9
            tupleOftuples += (float(temp), round(c, 2)),

    return tupleOftuples


"""
Given a tuple or a list of temperatures, this function returns a tuple of tuples.
Each tuple contains two values. The first is the value of the temperatures' parameter.
The second is the value of the [temperatures' parameter] converted to the unit of measurement
specified BY the input_unit_of_measurement parameter.

:param temperatures: An iterable containing temperatures
:param input_unit_of_measurement: The unit of measure to use to convert
the values in the temperatures parameter
:return: A tuple of tuples
"""
# pass  # remove pass statement and implement me

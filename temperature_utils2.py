def convert_to_kelvin(celsius_temp: float) -> int:
    celsius = int(input("Enter the Temperature in C:"))
    kelvin = celsius + 273.15
    print(str(celsius) + "degrees celsius is equal to " + str(int(kelvin)) + " degrees kelvin.")
    return kelvin
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(98)
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")

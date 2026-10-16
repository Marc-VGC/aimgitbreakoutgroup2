# temperature.py
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    temp_c = 25
    print(f"{temp_c}°C is equal to {celsius_to_fahrenheit(temp_c)}°F")
    
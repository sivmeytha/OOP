class Temperature:

    @staticmethod
    def celsuis_to_fahrenheit(celsius):
        return (9/5) * celsius + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return 9/5 * (fahrenheit - 32)

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

celsius = 25
fahrenheit = 100

print("Celsius: ", celsius)
print("Fahrenheit: ", Temperature.celsuis_to_fahrenheit(celsius))
print("Kelvin: ", Temperature.celsius_to_kelvin(celsius))
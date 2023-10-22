class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(temperature):
        return temperature * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(temperature):
        return (temperature - 32) * 5 / 9

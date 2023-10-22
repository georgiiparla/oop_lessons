class WeatherStation:
    __shared_attr = {
        "temperature": 0,
        "humidity": 0,
        "pressure": 0
    }

    def __init__(self):
        self.__dict__ = WeatherStation.__shared_attr

    def update_data(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def get_current_data(self):
        print(tuple(self.__dict__.values()))


sensor1 = WeatherStation()
sensor2 = WeatherStation()
sensor2.get_current_data()

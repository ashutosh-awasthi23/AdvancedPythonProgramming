from abc import ABC, abstractmethod


class SmartDevice(ABC):
    _name = ''
    _status = ''

    def __init__(self, name):
        self._name = name
        self._status = False


    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Light(SmartDevice):

    brightness = 0

    def __init__(self, name):
        super().__init__(name)
        # self._name = name
        # self._status = status

    def turn_on(self):
        self._status = 'on'
        return "Smart light is on."

    def turn_off(self):
        self._status = 'off'
        return "Smart light is off."

    def brightness_level(self, bright):
        self.brightness = bright
        return f"Brightness level set to {self.brightness}%"

    def device_info(self):
        return f"Light's name: {self._name}, Status: {self._status}"



class SmartThermostat(SmartDevice):

    def __init__(self,name):
        self._name = name
        self._status = False


    def turn_on(self):
        self._status=True
        return "SmartThermostat  is on."

    def turn_off(self):
        self._status=False
        return "SmartThermostat is off."

    def set_temperature(self,temp):
        print(f"Temperature set to {temp}")

    def device_info(self):
        return (f"Device info: {__class__.__name__}")









if __name__ == '__main__':

    bulb1 = Light("light1")

    print(bulb1.device_info())

    print(bulb1.turn_on())

    print(bulb1.device_info())

    print(bulb1.turn_off())

    print(bulb1.device_info())

    print(bulb1.brightness_level(1))

    st=SmartThermostat('st1')

    print(st.device_info())

    print(st.turn_on())

    print(st.device_info())

    print(st.turn_off())

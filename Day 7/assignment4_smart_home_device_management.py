#Smart Home device Management

from abc import ABC, abstractmethod


class SmartDevice(ABC):
    _name = ''
    _status = ''

    def __init__(self, name, status):
        self._name = name
        self._status = status

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Light(SmartDevice):

    brightness = 0

    def __init__(self, name, status):
        super().__init__(name, status)
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


if __name__ == '__main__':

    bulb1 = Light("light1", 'off')

    print(bulb1.device_info())

    print(bulb1.turn_on())

    print(bulb1.device_info())

    print(bulb1.turn_off())

    print(bulb1.device_info())

    print(bulb1.brightness_level(1))

# import numpy as np
# x=np.array([[1,2,3],[2,3,4],[7,8,9]],np.int64)
# print(x.shape)
# print(x.dtype)

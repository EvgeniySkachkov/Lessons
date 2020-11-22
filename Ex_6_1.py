from time import sleep
from itertools import cycle

class TrafficLight:
    __color = 'red'
    __COUNTER = 0
    __STOP = 21

    def running(self):
        for el in cycle([['red', 7], ['yellow', 2], ['green', 5]]):
            self.__color = el[0]
            print(self.__color)
            sleep(el[1])
            if self.__COUNTER == self.__STOP:
                break
            else:
                self.__COUNTER += 1


light = TrafficLight()
light.running()

from time import sleep


class TrafficLight:
    __color = ''

    def running(self):
        u_time = int(input('Сколько секунд удерживать зелёный свет на светофоре?: '))
        for _ in range(3):
            TrafficLight.__color = 'красный'
            print(TrafficLight.__color)
            sleep(7)
            TrafficLight.__color = 'жёлтый'
            print(TrafficLight.__color)
            sleep(2)
            TrafficLight.__color = 'зелёный'
            print(TrafficLight.__color)
            sleep(u_time)


light = TrafficLight()
light.running()

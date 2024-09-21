from time import sleep
import threading

class Knight(threading.Thread):
    aliens = 100
    lock = threading.Lock()

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f'{self.name} на нас напали!')
        while Knight.aliens > 0:
            Knight.aliens -= self.power
            self.days += 1
            print (f'{self.name}, сражается {self.days} день(дня)..., осталось {Knight.aliens} воинов.\n')
            sleep(1)
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)! \n')


first_knight = Knight('Sir Lancelot',10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')


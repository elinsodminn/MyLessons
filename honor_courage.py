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
        while True:
            with Knight.lock:
                if Knight.aliens <= 0:
                    break
                self.days += 1
                Knight.aliens -= self.power
                total_aliens = max(0, Knight.aliens)
                print (f'{self.name}, сражается {self.days} день(дня)..., осталось {total_aliens} воинов.' )
            sleep(1)
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

 
first_knight = Knight('Sir Lancelot',5)
second_knight = Knight('Sir Galahad', 10)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')

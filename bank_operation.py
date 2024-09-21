
from random import randint
import threading
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            one_dep = randint(50, 500)
            with self.lock:
                self.balance += one_dep
                print(f'Пополнение: {one_dep}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            one_trans = randint(50, 500)
            print(f'Запрос на {one_trans}')
            with self.lock:
                if one_trans < self.balance:
                    # self.lock.acquire()
                    self.balance -= one_trans
                    print(f'Снятие: {one_trans}. Баланс: {self.balance}')

                else:
                    print(f'Запрос отклонён, недостаточно средств')
            time.sleep(0.001)


bank = Bank()

deposit_thread = threading.Thread(target=Bank.deposit, args=(bank,))
take_thread = threading.Thread(target=Bank.take, args=(bank,))

deposit_thread.start()
take_thread.start()

deposit_thread.join()
take_thread.join()

print(f'Итоговый баланс: {bank.balance}')

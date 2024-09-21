from time import sleep
from datetime import datetime
from threading import Thread

# time_start = datetime.now()
def write_words(word_count, file_name):
    with open(file_name, 'wt+', encoding='utf-8') as file:
        i = 0
        while i != word_count:
            file.write(f'Какое-то слово № {i+1} \n')
            sleep(0.1)
            i += 1
        print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
print(f'Работа потоков {time_end - time_start} секунд')

time_start = datetime.now()
def thread_function(word_count, file_name):
    write_words(word_count, file_name)

threads = []
thread_data = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]

for word_count, file_name in thread_data:
    thread = Thread(target=thread_function, args=(word_count, file_name))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

time_end = datetime.now()
print(f'Работа потоков {time_end - time_start} секунд')

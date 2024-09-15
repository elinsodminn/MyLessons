from pprint import pprint
info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

def custom_write(file_name, strings):
    strings_pos = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):
            start_pos = file.tell()
            file.write(string + '\n')
            strings_pos[(i, start_pos)] = string
        pprint (strings_pos)

custom_write('test.txt', info)

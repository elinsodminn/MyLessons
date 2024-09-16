def add_everything_up(a, b):
    try:
        return(a + b)
    except TypeError:
        print('Сложить невозможно только склеить:')
        return(str(a) + str(b))

print(add_everything_up(123.456, 'Строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

def lenght_dif():
    first_zip = zip(first, second)
    first_list = list(first_zip)

    first_result = []
    for i, x in first_list:
             if  len(i) != len(x):
                 first_result.append(len(i) - len(x))
    print(first_result)

def lenght_eqv():
    second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
    result_list = list(second_result)
    print(result_list)

lenght_dif()
lenght_eqv()


first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
third_strings = first_strings + second_strings

sort_first_strings = sorted(first_strings, key=len)
sort_second_strings = sorted(second_strings, key=len)

def first_str ():
    first_result = []
    for fstr in first_strings:
        if len(fstr) >= 5:
            first_result.append(len(fstr))
    return first_result

def second_str ():
    second_result = []
    for i in sort_first_strings:
        for s in sort_second_strings:
            if len(i) == len(s):
                temp = (i, s)
                second_result.append(temp)
    return second_result

def third_str():
    third_result = {}
    for i in third_strings:
        if len(i) % 2 == 0:
            third_result[i] = len(i)
    return third_result

print(first_str())
print(second_str())
print(third_str())

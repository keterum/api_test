import re


my_list = ['123', '1', '12', 'test']
for element in my_list:
    if re.fullmatch(r'\d', element):
        print(element)

    '\d+'
    '\w[a-z]'

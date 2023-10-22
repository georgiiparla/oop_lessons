# isinstance(hello, str) - method to check belonging to the certain class

hello = 'Hello World!'
print(hello, 'Это строка?', isinstance(hello, str))
print(hello, 'Это bool?', isinstance(hello, bool))

my_list = [2, 4, 43]
print(my_list, 'Это список?', isinstance(my_list, list))

print(25, 'Это список?', isinstance(25, list))
print(25, 'Это целое число?', isinstance(25, int))

print(25, 'Это объект?', isinstance(25, object))
print(hello, 'Это объект?', isinstance(hello, object))
print(my_list, 'Это объект?', isinstance(my_list, object))

# Check memory locations of two instances (they take up different memory locations)

class Car:
    pass


a = Car()
b = Car()

print(id(a), a)  # id() to show id, and <__main__.Car object at 0x00000140A169E610> where 0x00000140A169E610 is the
# memory location
print(id(b), b)  # id() to show id, and <__main__.Car object at 0x00000140A169E650> where 0x00000140A169E650 is the
# memory location

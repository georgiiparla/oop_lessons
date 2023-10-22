class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "    555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


def checker(args):
    for word in args.split():
        print(f'{word}-YES' if hasattr(Person, word.lower()) else f'{word}-NO')


checker(input())

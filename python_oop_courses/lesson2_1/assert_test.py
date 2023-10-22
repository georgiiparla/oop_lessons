def courses_for_minors_only():
    age = int(input('Input you age please: '))
    assert age < 18, 'only for minors'
    return 'Welcome'


print(courses_for_minors_only())

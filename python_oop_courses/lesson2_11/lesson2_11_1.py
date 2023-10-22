class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        if isinstance(login, str):
            if all([login.count('@') == 1, login[login.index('@'):].count('.') > 0]):
                self.__login = login
            else:
                raise ValueError
        else:
            raise TypeError

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if isinstance(password, str):
            if all([4 < len(password) < 12,
                    Registration.is_include_digit(password),
                    Registration.is_include_all_register(password),
                    Registration.is_include_only_latin(password),
                    not Registration.check_password_dictionary(password)]):
                self.__password = password
            else:
                raise ValueError('Ваш пароль содержится в списке самых легких')
        else:
            raise TypeError("Пароль должен быть строкой")

    @staticmethod
    def is_include_digit(string: str):
        cnt = 0
        for i in string:
            if i in '0123456789':
                cnt += 1
        if cnt:
            return True
        else:
            raise ValueError('Пароль должен содержать хотя бы одну цифру')

    @staticmethod
    def is_include_all_register(string: str):
        cnt_u = 0
        cnt_l = 0
        for i in string:
            if i in 'abcdefghijklmnopqrstuvwxyz'.upper():
                cnt_u += 1
            elif i in 'abcdefghijklmnopqrstuvwxyz':
                cnt_l += 1
        if cnt_u and cnt_l:
            return True
        else:
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')

    @staticmethod
    def is_include_only_latin(string: str):
        for i in string:
            if i.lower() not in 'abcdefghijklmnopqrstuvwxyz0123456789':
                raise ValueError('Пароль должен содержать только латинский алфавит')
            else:
                return True

    @staticmethod
    def check_password_dictionary(string: str):
        with open("easy_passwords.txt", "r", encoding="utf-8") as file:
            if string in [line.strip() for line in file]:
                return True
            else:
                return False


try:
    s2 = Registration("fga", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fga', 'asd12') как можно записать такой логин?")

try:
    s2 = Registration("fg@a", "asd12")
except ValueError as e:
    pass
else:
    raise ValueError("Registration('fg@a', 'asd12') как можно записать такой логин?")

s2 = Registration("translate@gmail.com", "as1SNdf")
try:
    s2.login = "asdsa12asd."
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12asd как можно записать такой логин?")

try:
    s2.login = "asdsa12@asd"
except ValueError as e:
    pass
else:
    raise ValueError("asdsa12@asd как можно записать такой логин?")

assert Registration.check_password_dictionary('QwerTy123'), 'проверка на пароль в слове не работает'

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 хранится в словаре паролей, как его можно было сохранить?")


try:
    s2.password = "KissasSAd1f"
except ValueError as e:
    pass
else:
    raise ValueError("KissasSAd1f хранится в словаре паролей, как его можно было сохранить?")

try:
    s2.password = "124244242"
except ValueError as e:
    pass
else:
    raise ValueError("124244242 пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "RYIWUhjkdbfjfgdsffds"
except ValueError as e:
    pass
else:
    raise ValueError("RYIWUhjkdbfjfgdsffds пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "CaT"
except ValueError as e:
    pass
else:
    raise ValueError("CaT пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "monkey"
except ValueError as e:
    pass
else:
    raise ValueError("monkey пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = "QwerTy123"
except ValueError as e:
    pass
else:
    raise ValueError("QwerTy123 пароль есть в слове, нельзя его использовать")

try:
    s2.password = "HelloQEWq"
except ValueError as e:
    pass
else:
    raise ValueError("HelloQEWq пароль НЕОЧЕНЬ, как его можно было сохранить?")

try:
    s2.password = [4, 32]
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

try:
    s2.password = 123456
except TypeError as e:
    pass
else:
    raise TypeError("Пароль должен быть строкой")

print('U r hacked Pentagon')

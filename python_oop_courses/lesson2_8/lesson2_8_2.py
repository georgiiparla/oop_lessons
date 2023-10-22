class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def date(self):
        day = str(self.day)
        month = str(self.month)
        year = str(self.year)
        while len(day) != 2:
            day = '0' + day
        while len(month) != 2:
            month = '0' + month
        while len(year) != 4:
            year = '0' + year
        return f'{day}/{month}/{year}'

    @property
    def usa_date(self):
        day = str(self.day)
        month = str(self.month)
        year = str(self.year)
        while len(day) != 2:
            day = '0' + day
        while len(month) != 2:
            month = '0' + month
        while len(year) != 4:
            year = '0' + year
        return f'{month}-{day}-{year}'


d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date) # 05/10/2001
print(d1.usa_date) # 10-05-2001
print(d2.date) # 15/03/0999
print(d2.usa_date) # 03-15-0999

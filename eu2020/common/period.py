import eu2020.data.data as data


class Period:

    def __init__(self, year, month):
        self.year = year
        self.month = month


    def next(self):
        self.month = self.month + 1
        if self.month == len(data.months):
            self.month = 0
            self.year = self.year + 1


    def get_year(self):
        return self.year


    def get_month(self):
        return data.months[self.month]

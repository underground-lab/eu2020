import eu2020.data.data as data


class Period:

    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month

    def next(self) -> None:
        self.month += 1
        if self.month == len(data.months):
            self.month = 0
            self.year += 1

    def get_year(self) -> int:
        return self.year

    def get_month(self) -> str:
        return data.months[self.month]

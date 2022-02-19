import datetime as dt


# For each function class need a docstring to explain usage of that.
# For the Record class I will write it as an example and please add docstring for left classes.
# In PEP standards need two empty lines before class declaration.


class Record:
    def __init__(self, amount, comment, date=''):
        """
        Class is aimed to record 'amount' of money 'date' of spent and how have been spent money 'comment'.

        Parameters
        ----------
        amount : int
            Presents amount spent money.
        comment : str
            For what have been spent money.
        date : str
            Date of spent.
        """
        self.amount = amount
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        # Add docstrings for this class.
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        # Change iterator name of the for loop below. It is not a proper way to iterate using class name as an iterator
        # because iterator in this case is a item of the self.records list which type is int and int has no
        # date(Record.date) attribute.For example
        # for spent in self.records:
        #    ...
        for Record in self.records:
            # Here need to be created an object of the Record class. And object count will be equal to len(self.records)
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # This if statement can be simplified using style mentioned bellow comment.
            # (7 > (today - record.date).days >= 0)
            if (
                    (today - record.date).days < 7 and
                    (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        x = self.limit - self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        else:
            return ('Хватит есть!') # In this line for return need not use parentheses.


class CashCalculator(Calculator):
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    # In Python argument name should be lowercase. For instance, usd_rate
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # Statement seems to have no effect. It means for assigning we use only one equal sign (x = 10)
            cash_remained == 1.00
            currency_type = 'руб'
        # In each line you have written currency_type == smth.I would suggest to use currency_type.upper().
        # And before returning cash_remained in this string  f'{currency_type}' will be appeared USD, РУБ, or EURO
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    def get_week_stats(self):
        super().get_week_stats()
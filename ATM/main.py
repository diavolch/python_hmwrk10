# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


class ATM:

    def __init__(self, total_cash=0, count=0):
        self.__total_cash = total_cash
        self.__count = count

    def print_balance(self):
        print(f'На балансе {self.__total_cash} рублей')

    def percents_for_third(self):
        if self.__count == 3:
            self.__total_cash += self.__total_cash * 0.03
            self.__count = 0
        else:
            self.__count += 1

    def replenish(self, cash):
        if cash % 50 == 0:
            self.__total_cash += cash
            self.percents_for_third()
        else:
            print('Введите сумму, кратную 50')

    def withdraw(self, cash):
        if cash % 50 == 0:
            percent = cash * 0.015
            if percent < 30:
                percent = 30
            if percent > 600:
                percent = 600
            if self.__total_cash < (cash + percent):
                print("недостаточно средств")
            else:
                self.__total_cash -= (cash + percent)
                self.percents_for_third()
        else:
            print('Введите сумму, кратную 50')


c1 = ATM()
c1.replenish(200)
c1.print_balance()
c1.withdraw(50)
c1.print_balance()
c1.withdraw(30)
c1.print_balance()
#!/usr/bin/env python

class Account(object):
        counter = 0
        def __init__(self, holder, number, balance,credit_line=1500):
            Account.counter += 1
            self.Holder = holder
            self.Number = number
            self.Balance = balance
            self.CreditLine = credit_line

        def deposit(self, amount):
            self.Balance = amount

        def withdraw(self, amount):

            if (self.Balance - amount < -self.CreditLine):
                return False
            else:
                self.Balance -= amount
                return True

        def balance(self):
            return self.Balance

        def transfer(self, target, amount):
            if (self.Balance - amount < -self.CreditLine):
                return False
            else:
                self.Balance -= amount
                target.Balance += amount
                return True

        def __del__(self):
            Account.counter -= 1

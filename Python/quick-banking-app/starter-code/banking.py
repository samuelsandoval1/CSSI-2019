#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
        # self.withdraw = withdraw
        # self.deposit = deposit
        # self.rename = rename
    def __str__(self):
        return '{self.label}\'s bank account. The balance {self.balance}.'.format(self=self)

    def withdraw(self, amount):
        name = ""
        while(balance-amount < 0):
            amount = raw_input("Enter amount to be withdrawn: ")
        self.balance -= amount
        print"You Withdrew:" + str(self.balance)

    def deposit(self, amount):
        name = ""
        while(balance-amount < 0):
            amount = raw_input("Enter amount to be withdrawn: ")
        self.balance += amount
        print "Amount withdraw:" + str(self.balance)

    def rename(self, name):
        name = ""
        while(name == ""):
            name = raw_input("Enter a new name for the Bank Account: ")
        print "Amount :" + str(self.balance)
        self.label=name

    def transfer (self, dest_account, account):
        name = ""
        while(name == ""):
            name = raw_input("Enter a transfer place Bank Account: ")

        self.label=account
        pass

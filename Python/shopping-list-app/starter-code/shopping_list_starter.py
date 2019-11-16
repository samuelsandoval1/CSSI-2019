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

choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")

    choice = raw_input("Enter your choice [a|b|c|d|e]:")


    # Your code below! Handle the cases when the user chooses a, b, c, d, or e

#a - e
    if choice == "a":
        item = raw_input("Please enter item: ")
        shopping_list.append(item)
    elif choice == "b":
        item = raw_input("Please type item that you want removed: ")
        shopping_list.remove(item)
    elif choice == "c":
        item = raw_input("Please state the item you search for: ")
        if item in shopping_list:
            print(item + " is on the shopping list.")
        else:
            print(item + " is not on the shopping list.")
    elif choice == "d":
        print shopping_list
    elif choice == "e":
        print("Goodbye")
    else:
        print("Please enter a correct choice [a|b|c|d|e]")

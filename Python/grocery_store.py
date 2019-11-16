shopping_list = raw_input("Hello, what would you like to buy: ").split(", ")

class Item(object):
    def __init__(self, name, price, inventory, is_taxable):
        self.name = name
        self.price = price
        self.inventory = inventory
        self.is_taxable = is_taxable

store = {
     "banana": Item("banana", 8, 10, False),
     "bread": Item("bread", 3, 10, False),
     "eggs": Item("eggs", 10, 1, True)

}


# DICTIONARIES BELOW
# prices = {
#     'banana' : 8,
#     'bread' : 3,
#     'eggs' : 10,
#     'watermelon' : 1,
#     'chocolate milk' : 5,
#     'nutritional yeast' : 8,
#     'chicken' : 6,
#     'pizza' : 7,
#     'cereal' : 7,
#     'juice' : 6
# }
#
# inventory = {
#     'banana' : 10,
#     'bread' : 10,
#     'eggs' : 10,
#     'watermelon' : 20,
#     'chocolate milk' : 20,
#     'nutritional yeast' : 10,
#     'chicken' : 0,
#     'pizza' : 20,
#     'cereal' : 20,
#     'juice' : 10
# }

# taxable = ['eggs' , 'nutritional yeast']

total = 0
for item in shopping_list:
    if item in store and store[item].inventory > 0:
        if store[item] is_taxable:
            total += store[item].price *1.0
            # # <= 0:
            #Ω print("There are no more " + item)
        else:
            total += store[item].price
        store[item] -= 1
            # inventory[item] -= 1
            # print("The inventory of " + item + " remaining is " + str(inventory[item]))
            # total += prices[item] + (prices[item]*0.0725)
            # print "The current total is " + str(total)

    # print inventory[item]

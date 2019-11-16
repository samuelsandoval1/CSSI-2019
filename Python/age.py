def printCanVote(age):
    if age >= 18:
        print'You can vote!'
    elif age >= 16:
        print'You can drive!'
    else:
        print 'Not old enough for voting or driving'

name = raw_input("Enter your name: ")

while name != "quit":
    age = int(raw_input("Enter your age: "))
    printCanVote(age)
    name = raw_input("Enter your name (quit to exit)")

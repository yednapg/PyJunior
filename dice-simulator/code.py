import random

while True:
    print('1. roll the dice  2. exit')
    user = int(input("What you want to do\n"))

    if user == 1:
        number = rndom.randint(1,6)
        print(number)
    else:
        break
num = 7
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("Not Prime")
            break
        else:
            print("It's Prime")
else:
    print("Not Prime")
import random                         # Program that generates random numbers from 1 to 6 so that it can work like a dice simulator
def rolling_dice(minimum=1,maximum=6):
    while True:
        if input('Do you want to roll the dice ? type y/n: ').lower()=='n':
            break
        else:
            print(random.randint(minimum,maximum))
rolling_dice()

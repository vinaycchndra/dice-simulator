import random 
def rolling_dice(minimum=1,maximum=6):
    while True:
        if input('Do you want to roll the dice ? type y/n: ').lower()=='n':
            break
        else:
            print(random.randint(minimum,maximum))
rolling_dice()
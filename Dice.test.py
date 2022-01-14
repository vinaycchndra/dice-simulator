import random 
# Program that generates random numbers from 1 to 6 so that it can work like a dice simulator
class dice_roll:
    
    def __init__(self,bias='n',inclined=0):
        self.bias = bias
        self.inclined = inclined
        
    def calling_function(self):
        if self.bias.lower() == 'y':
            return self.rolling_dice_biased()
        else:
            return self.rolling_dice_unbiased()
    
    def rolling_dice_biased(self,minimum=1,maximum=6):
        print(random.randint(minimum,maximum))
        print('biased')
        arr = []
        i = 0
        while i<100000:
            a = random.randint(minimum,maximum)
            b = random.randint(minimum,maximum)
            if b==self.inclined:
                arr.append(b)
            else:
                arr.append(a)
            i+=1
        return arr
            
    def rolling_dice_unbiased(self,minimum=1,maximum=6):
        print(random.randint(minimum,maximum))
        print('unbiased')
        arr = []
        i = 0
        while i<100000:
            a = random.randint(minimum,maximum)
            arr.append(a)    
            i+=1
        return arr
biased = input('Hey! do you want baised? Y/N: ')
if biased.lower()=='y':
    inclined = int(input('Which number you want to appear more from 1 to 6? :'))
    roll = dice_roll(biased,inclined)
else:
    roll = dice_roll()
arr = roll.calling_function()
for _ in range(1,7):
    print(f'{_} appeared for {arr.count(_)} out of 100000 of dice rolls')
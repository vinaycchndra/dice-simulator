import random                                                      # Dice simulator
class dice_roll:
    
    def __init__(self,bias='n',inclined=0):
        self.bias = bias
        self.inclined = inclined
        
    def calling_function(self):                                    # Function for calling unbiased or biased die
        if self.bias.lower() == 'y':
            self.rolling_dice_biased()
        else:
            self.rolling_dice_unbiased()
    
    def rolling_dice_biased(self,minimum=1,maximum=6):             # Biased die simulator function
        print(random.randint(minimum,maximum))
        while True:
            if input('Do you want to roll again the dice ? type Y/N: ').lower()=='n':
                return 
            else:
                a = random.randint(minimum,maximum)
                b = random.randint(minimum,maximum)
                if b==self.inclined:                                # Condition that increases the probability of the appearance of the number
                    print(b)
                else:
                    print(a)
                    
    def rolling_dice_unbiased(self,minimum=1,maximum=6):            # Unbiased die simulator
        print(random.randint(minimum,maximum))
        while True:
            if input('Do you want to roll again the dice ? type Y/N: ').lower()=='n':
                return  
            else:
                a = random.randint(minimum,maximum)
                print(a)
                
                
biased = input('Hey! do you want baised die? Y/N : ')
if biased.lower()=='y':
    inclined = int(input('Which number you want to appear more from 1 to 6? :'))
    roll = dice_roll(biased,inclined)
else:
    roll = dice_roll()
roll.calling_function()                                               # Method to call the function
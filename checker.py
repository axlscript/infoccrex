import random
from cores import *

live = True
false = False
resultado_checker = False


resultado_checker = random.choice([live, false])


def checkerTrue():
    if resultado_checker == True:
        print(f'Status: {Verde}Live{Reset}') 

    else:
        print(f'Status: {Vermelho}Die {Reset}(Tente novamente)')
        

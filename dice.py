#Dice simulator
from random import randint
result=randint(1,6)
while(True):
    result = randint(1,6)
    # This will pick a random number between 1 and 6.
    if(result==1):
        print(' ----------')
        print('|          |')
        print('|    o     |')
        print('|          |')
        print(' ----------')
    elif(result==2):
        print(' ----------')
        print('|    o     |')
        print('|          |')
        print('|    o     |')
        print(' ----------')
    elif(result==3):
        print(' ----------')
        print('|    o     |')
        print('|          |')
        print('|  o    o  |')
        print(' ----------')
    elif(result==4):
        print(' ----------')
        print('| o      o |')
        print('|          |')
        print('| o      o |')
        print(' ----------')
    elif(result==5):
        print(' ----------')
        print('| o      o |')
        print('|    o     |')
        print('| o      o |')
        print(' ----------')
    else:
        print(' ----------')
        print('| o      o |')
        print('| o      o |')
        print('| o      o |')
        print(' ----------')
    n=input("Again You need to roll a dice:")
    if(n=='Yes' or n=='yes' or n=='Yah' or n=='yah'):
        continue
    else:
        break

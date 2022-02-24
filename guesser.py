import random

def setNum():
    return random.randint(1,20)

def Attempt():
    dis = 0
    best = 0
    num = setNum()
    attempts = int(input('\nHow many attempts do you think you need to guess a random number between 1 and 20? \n\n'))
    for i in range (attempts):
        if i == 0:
            choice = int(input("\nSo, the number is...?\n\n"))
        
        else:
            choice = int(input(f'You have {attempts-i} more attempts! Good luck \n\n'))
        dis = choice - num
        best = abs(dis)
        if dis <= best:
           best = dis

        if choice < 1 or choice > 20:
            print ('\nYou trolled my game :(\n')
            break

        if choice == num:
            print('\nWow, you might be a wizard!\n')
            break

        else:
            str = ''
            if choice < num and i != attempts-1:
                str = 'bigger'

            elif choice > num and i != attempts-1:
                str = 'smaller'
            print(f'\nNope, Try a {str} number\n')

    print(f'The number was {num}!\n')
    if best != 0:
        print (f'You missed by {abs(best)} at your best attempt.\n\n')
    
    restart = input('Type "1" if you want to play more and something else to stop playing: ')
    if restart == '1':
        Attempt()
            

        
Attempt()
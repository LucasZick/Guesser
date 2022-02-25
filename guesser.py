import random

play = 1

def attempt(possib):
    return random.choice(possib)

def defineChances():
    print ('________________________________________________________')
    chances = int(input('\nHow many chances do I have to find your secret number?\n'))
    print ('________________________________________________________')
    return chances

def defineMaxim():
    maxim = int(input('\nWhat is the range of your choice?\n'))
    print ('________________________________________________________')
    return maxim

def numbers(maxim):
    possib = []
    for i in range(maxim):
        possib.append(i+1)
    return possib

def run():
    chances=defineChances()
    maxim=defineMaxim()
    poss=numbers(maxim)
    for i in range(chances):
        attemp = attempt(poss)
        ind = poss.index(attemp)
        if len(poss)==1:
            print(f'\nYour number is {poss[0]}! Did it in {i} attempts\n')
            break
        print (f'________________________________________________________\n\nI still have {chances-i} attempts, and I guess your number is {attemp}')
        result = int(input('\n    1 -- that is too small\n    2 -- that is too big\n    3 -- that is my number!\n\n'))
        if result == 1:
            try:
                poss = poss[ind+1:]
            except ValueError:
                print('Why are you trying to fool me?')

        elif result == 2:
            try:
                poss = poss[:ind]
            except ValueError:
                print('Why are you trying to fool me?')

        elif result == 3:
            try:
                poss = [attemp]
            except ValueError:
                print('Stop kidding me! ')
    print ('________________________________________________________')
    print ('________________________________________________________\n')

while play != 0:
    run()
    play=int(input('Do you want to play more? \n\n                 0 -- No\n    Something else -- Yes\n\n'))
    print ('________________________________________________________')
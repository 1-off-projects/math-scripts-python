# imports

import random, os

# screen clear func

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

# guessgame/main

clrscr()
print("welcome to the guessing game\nguess two numbers from the inputs you provide...")
while True:
    m1: int = int(input("minimum it can be: ")) 
    clrscr()
    m2: int = int(input("maximum it can be: "))
    truenum: int = int(random.randint(m1, m2))
    clrscr()
    while True:    
        guess: int = int(input("what is your guess: "))
        if str(guess) == str(truenum):
            again: str = str(input("correct. again? [y/n]"))
            if again == 'y':
                break
            else:
                clrscr()
                quit()
        elif int(guess) < int(truenum):
            clrscr()
            print("wrong, more!")
        elif int(guess) > int(truenum):
            clrscr()
            print("wrong, less!")
        else:
            clrscr()
            print("so incorrect that it errored!!")
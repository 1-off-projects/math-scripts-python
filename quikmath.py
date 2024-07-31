import random, os
numrounds = 0
score = 0
def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')
clrscr()
print("dificulty selection")
print("1. baby (5 max)")
print("2. easy (10 max)")
print("3. medium (15 max)")
print("4. hard (20 max)")
dif = input("select 1-4: ")
if dif == '1':
    max = 5
elif dif == '2':
    max = 10
elif dif == '3':
    max = 15
    print("maximum set to 15")
elif dif == '4':
    max = 20
else:
    print("invalid choice")
    exit
clrscr()
rounds = input("how many questions?")
clrscr()
print("menu")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. devide")
choice = input("enter 1-4: ")
clrscr()
if choice == '1':
    print("you picked adding.")
    while True:
        if int(numrounds) < int(rounds):
            num1 = random.randint(1,max)
            num2 = random.randint(1,max)
            print(num1, "+", num2, "= ")
            answer = input("")
            clrscr()
            trueans = int(num1+num2)
            if float(answer) == round(float(trueans)):
                print("correct!")
                score += 1
                numrounds += 1
            else:
                print("incorrect")
                numrounds += 1
        else:
            break
        break
    clrscr()
    print(f"you got {score}/{numrounds} correct!")
elif  choice == '2':
    print("you picked subtracting.")
    while True:
        if int(numrounds) < int(rounds):
            num1 = random.randint(1,max)
            num2 = random.randint(1,max)
            print(num1, "-", num2, "= ")
            answer = input("")
            clrscr()
            trueans = int(num1-num2)
            if float(answer) == round(float(trueans)):
                print("correct!")
                score += 1
                numrounds += 1
            else:
                print("incorrect")
                numrounds += 1
        else:
            break
        break
    clrscr()
    print(f"you got {score}/{numrounds} correct!")
elif choice == '3':
    print("you picked multiplying.")
    while True:
        if int(numrounds) < int(rounds):
            num1 = random.randint(1,max)
            num2 = random.randint(1,max)
            print(num1, "*", num2, "=")
            answer = input("")
            clrscr()
            trueans = int(num1*num2)
            if float(answer) == round(float(trueans)):
                print("correct!")
                score += 1
                numrounds += 1
            else:
                print("incorrect")
                numrounds += 1
        else:
            break
        break
    clrscr()
    print(f"you got {score}/{numrounds} correct!")
elif choice == '4':
    print("you picked deviding answer is closest whole number.")
    while True:
        if int(numrounds) < int(rounds):
            num1 = random.randint(1,max)
            num2 = random.randint(1,max)
            print(num1, "/", num2, "= ")
            float: answer = input("")
            clrscr()
            trueans = float(num1/num2)
            if float(answer) == round(float(trueans)):
                print("correct!")
                score += 1
                numrounds += 1
            else:
                print("incorrect")
                numrounds += 1
        else:
            break
        break
    clrscr()
    print(f"you got {score}/{numrounds} correct!")
else:
    print("goodbye")
    exit
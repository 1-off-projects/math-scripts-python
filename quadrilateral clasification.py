# start
print("main menu")
print("y = yes")
print("n = no")
choice = input("does it have 4 right angles? ")
if choice == 'y':
    print("y = yes")
    print("n = no")
    choice = input("does it have 4 equal sides? ")
    if choice == 'y':
        print("its a square")
    elif choice == 'n':
        print("its a rectangle")
    else:
        pass
elif choice == 'n':
    print("y = yes")
    print("n = no")
    choice = input("does it have a pair of parallel sides? ")
    if choice == 'y':
        print("y = yes")
        print("n = no")
        choice = input("does it have two pairs of parallel sides? ")
        if choice == 'y':
            print("y = yes")
            print("n = no")
            choice = input("are all sides the same length? ")
            if choice == 'y':
                print("its a rhombus")
            if choice == 'n':
                print("its a parallelogram")
        elif choice == 'n':
            print("its a trapazoid")
    elif choice == 'n':
        print("its a quadrilateral")
else:
    pass
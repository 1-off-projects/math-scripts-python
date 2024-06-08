import math
print("Menu:")
print("1.start with circumfrence: ")
print("2.start with diameter: ")
print("3.start with radius: ")
choice = input("selection: ")
if choice == '1':
    circum = input("enter circumfrence: ")
    diam = float((float(circum)/math.pi))
    rad = float(diam/2)
    diameter = (str("diameter: ")) + str(diam)
    radius = (str("radius: ")) + str(rad)
    print(diameter)
    print(radius)
elif choice == '2':
    diam = float(input("enter diameter: "))
    circum = float(diam*math.pi)
    rad = float(diam/2)
    circumfrence = (str("circumfrence: ") + str(circum))
    radius = (str("radius: ")) + str(rad)
    print(circumfrence)
    print(radius)
elif choice == '3':
    rad = input("enter radius: ")
    diam = float(rad*2)
    circum = float(diam*math.pi)
    diameter = (str("diameter: ")) + str(diam)
    circumfrence = ("circumfrence: ") + str(circum)  
    print(diameter)
    print(circumfrence)
else:
    pass
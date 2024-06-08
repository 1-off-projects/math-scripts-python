import math
# prompt for triangle
side1 = int(input("side 1 "))
side2 = int(input("side 2 "))
angle1 = int(input("angle 1 "))
angle2 = int(input("angle 2 "))
angle3 = int(180) - int(angle1 + angle2)
a2 = int(int(side1)*int(side1))
b2 = int(side2*side2)
c2 = int(a2+b2)
side3 = math.sqrt(c2)
if angle1 or angle2 or angle3 == 90:
    triangle_angles = 'right'
elif angle1 or angle2 or angle3 < 90:
    triangle_angles = 'obtuse'
elif angle1 or angle2 or angle3 > 90:
    triangle_angles = 'acute'
elif angle1 or angle2 or angle3 <= 180:
    print('pick a valid angle size')
else:
    pass
if side1 == side2:
    triangle_sides = 'isosceles'
elif side1 == side2 == side3:
    triangle_sides = 'equalateral'
else:
    triangle_sides = 'scalene'
print(("it's a ") + (triangle_angles) + (", ") + (triangle_sides) + (" triangle!"))
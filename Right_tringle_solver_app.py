import math

print('Welcome to the Right Triangle Solver App')
f_leg = float(input('\nWhat is the first leg of the triangle:'))
s_leg = float(input('What is the second leg of the triangle:'))
hypotenuse = round(math.sqrt(((f_leg)**2) + ((s_leg)**2)),3)
area = round(0.5*f_leg*s_leg,3)
print(f'For a triangle with legs f {f_leg} and {s_leg} the hypotenuse is {hypotenuse}')
print(f'For a triangle with legs f {f_leg} and {s_leg} the area is {area}')
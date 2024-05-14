#Cesar Flores
#04/14/24
#P2LAB1_FloresCesar
# Using math expressions
import math
radius = float(input("What is radius of the circle?"))
cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)
print(f'The diameter of the circle is {diam:.1f}')
print(f'The circumference of the circle is {cir:.2f}')
print(f'The area of the circle is {area:.3f}')

import numeric.e1.resistance as resistance
import numeric.e1.cosine as cosine

import random
from math import pi


# print("Resistance\n\n")
#
# print("   --R1-------R2--")
# print("   |             |")
# print("A--|             |--B")
# print("   |             |")
# print("   --R3-------R4--")
#
# r1 = float(input("R1 = "))
# r2 = float(input("R2 = "))
# r3 = float(input("R3 = "))
# r4 = float(input("R4 = "))
#
# print("total resistance = ", resistance.get_total_resistance_left(r1, r2, r3, r4))
#
# print()
#
# print("   ---R1---   ---R2---")
# print("   |      |   |      |")
# print("A--|      |---|      |--B")
# print("   |      |   |      |")
# print("   ---R3---   ---R4---")
#
# r1 = float(input("R1 = "))
# r2 = float(input("R2 = "))
# r3 = float(input("R3 = "))
# r4 = float(input("R4 = "))
#
# print("total resistance = ", resistance.get_total_resistance_right(r1, r2, r3, r4))
#
# counter = 0
# for i in range(10000):
#     r1 = random.uniform(0, 100)
#     r2 = random.uniform(0, 100)
#     r3 = random.uniform(0, 100)
#     r4 = random.uniform(0, 100)
#     left = resistance.get_total_resistance_left(r1, r2, r3, r4)
#     right = resistance.get_total_resistance_right(r1, r2, r3, r4)
#     if left < right:
#         counter += 1
# print("The left configuration has been smaller in", counter, "of 10,000 cases.")

print()
print("Cosine Series\n\n")

arguments = [i*pi for i in range(21)]
cosine.list_cosine_values(arguments)
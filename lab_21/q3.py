"""Write a program to convert a tuple of angles into a list of tuples with each tuple containing
the sine and cosine of an angle"""
import math
def convert_angles_to_sin_cos(angles, in_degrees=True):

    result = []
    for angle in angles:

        rad = math.radians(angle) if in_degrees else angle

        sin_val = round(math.sin(rad), 4)
        cos_val = round(math.cos(rad), 4)

        result.append((sin_val, cos_val))

    return result
angles_tuple = (0, 30, 45, 60, 90)
output = convert_angles_to_sin_cos(angles_tuple, in_degrees=True)
print("Original Angles (degrees):", angles_tuple)
print("List of (sin, cos) tuples:", output)
#or
import math

angles = (0, math.pi / 6, math.pi / 4, math.pi / 2)
sin_cos_list = [(round(math.sin(a), 4), round(math.cos(a), 4)) for a in angles]

print(sin_cos_list)



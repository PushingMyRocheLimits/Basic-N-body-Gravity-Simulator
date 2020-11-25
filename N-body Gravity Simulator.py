# Rudimentary N-body Gravity Simulator by Levi Van Ryder
from vpython import *
import random


# Calculates the forces that two objects experience
def cal_force(star1, star2):
    g = 6.67e-11
    r_vector = star1.pos - star2.pos
    r_magnitude = mag(r_vector)
    r_hat = r_vector / r_magnitude
    force_magnitude = g * star1.mass * star2.mass / r_magnitude ** 2
    force_vector = -force_magnitude * r_hat
    return force_vector


# Number of stars that will be generated
num_stars = int(input("How many stars?: "))

# Time and ROC of Time
dt = 0.001
t = 0

# Lists for data storage
star_pos_data = []
star_mass_data = []

# Generates star data
for x in range(num_stars):
    star = sphere(pos=vector(random.randrange(0, 100), random.randrange(0, 100), random.randrange(0, 100)),
                  radius=random.randrange(1, 3), color=color.yellow, mass=random.randrange(1000, 5000),
                  momentum=vector(random.randrange(1, 5), random.randrange(1, 5), random.randrange(1, 5)),
                  make_trail=True)
    star_pos_data.append(star.pos)
    star_mass_data.append(star.mass)

print(star_pos_data)
print(star_mass_data)

#while true:
 #  rate(500)
  # for x in star_data:

"""  Rudimentary N-body Gravity Simulator by Levi Van Ryder
                              Written in Python 3.8.5                               """
from vpython import *
import random

# Calculates the forces that two stars experience 
def cal_force (p1, p2):
    G = 6.67e-11
    r_vector = (p1.pos - p2.pos)
    r_magnitude = mag(r_vector)
    r_hat = (r_vector / r_magnitude)
    force_magnitude = ((G * p1.mass * p2.mass) / (r_magnitude ** 2))
    force_vector = (-force_magnitude * r_hat)
    return force_vector

# Number of stars that will be generated
num_stars = int(input("How many stars?: "))

""" I barely managed to perform the simulations with 50 stars with my PC (Intel core i3 & Nvidia GeForce GTX 950)"""

# ROC of Time
dt = 1000

# Variable for data storage
stars_data = [ ]
momentum_sum = vec(0, 0, 0)

# Generates star data
for i in range(num_stars):
    star = sphere(pos=vector(random.randrange(-5000, 5000), random.randrange(-5000, 5000), random.randrange(-5000, 5000)),
                    mass=random.randrange(100000, 500000), color=color.yellow, momentum=vector(random.randrange(-10, 10),
                    random.randrange(-10, 10), random.randrange(-10, 10)),
                   make_trail=True, trail_radius=3)
    star.radius = star.mass / 10000
    stars_data.append(star)
    momentum_sum = momentum_sum + star.momentum

# Adds up momentum for each star
for i in range(num_stars):
    stars_data[i].momentum = (stars_data[i].momentum + (momentum_sum / num_stars))

# Performs the simulation 
while True:
    rate(1000)
    L = len(stars_data)
    for i in range(L):
        stars_data_i = stars_data[i]
        force = vec(0, 0, 0)
        for j in range(L):
            if i == j: continue
            stars_data_j = stars_data[j]
            force = force + cal_force(stars_data_i, stars_data_j)
        stars_data_i.momentum = (stars_data_i.momentum + (force * dt))
        for star in stars_data:
            if star == None: continue
            star.pos = (star.pos + (star.momentum * (dt / star.mass)))

""" Base Project Completed on November 1, 2020 """


"""  Rudimentary N-body Gravity Simulator by Levi Van Ryder
                    Written in Python 3.8.5                               """
from vpython import *
import random

# Canvas for simulation
scene = canvas(title='N-body Gravity Simulator', width=1920, height=1080, caption='Created by PushingMyRocheLimits')

# Axis for reference and initial camera angle
x = cylinder(pos=vector(0, 0, 0), axis=vector(1, 0, 0), size=vector(10000, 10, 10), color=color.white, opacity=0.5)
x_neg = cylinder(pos=vector(0, 0, 0), axis=vector(-1, 0, 0), size=vector(10000, 10, 10), color=color.white, opacity=0.5)
label(pos=x.axis, text='x', font='serif')
label(pos=x_neg.axis, text='x', font='serif')
y = cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), size=vector(10000, 10, 10), color=color.white, opacity=0.5)
y_neg = cylinder(pos=vector(0, 0, 0), axis=vector(0, -1, 0), size=vector(10000, 10, 10), color=color.white, opacity=0.5)
label(pos=y.axis, text='y', font='serif')
label(pos=y_neg.axis, text='y', font='serif')
z = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 1), size=vector(10000, 10, 10), color=color.white, opacity=0.5)
z_neg = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, -1), size=vector(10000, 10, 10), color=color.white, opacity=0.5)
label(pos=z.axis, text='z', font='serif')
label(pos=z_neg.axis, text='z', font='serif')
scene.camera.pos = vector(1000, 500, 100)

# Calculates the forces that two stars experience (Newton's Law of Universal Gravitation vector form)
def cal_force (p1, p2):
    G = 6.67e-11
    r_vector = (p1.pos - p2.pos)
    r_magnitude = mag(r_vector)
    r_hat = (r_vector / r_magnitude)
    force_magnitude = ((G * p1.mass * p2.mass) / (r_magnitude ** 2))
    force_vector = (-force_magnitude * r_hat)
    return force_vector

# Variable for data storage
stars_data = []
momentum_sum = vec(0, 0, 0)

# Number of stars that will be generated
num_stars = int(input("How many stars?: "))

# Asks user whether they want random values for stars or to manually enter in values
'''Demo mode plugs in random values for the stars and Manual allows for custom data entry'''
user_setting = input("For random values, enter 'Demo'. For manual values, enter in 'Manual': ")
if user_setting.lower() == 'manual':
    for i in range(num_stars):
        star = sphere(pos=vector(int(input("X Position: ")), int(input("Y Position: ")), int(input("Z Position: "))),
                mass=int(input("Mass of Star: ")), color=color.yellow, momentum=vector(int(input("X Velocity: ")),
                int(input("Y Velocity: ")), int(input("Z Velocity: "))), make_trail=True, trail_radius=3)
        star.radius = star.mass / 10000
        stars_data.append(star)
        momentum_sum = momentum_sum + star.momentum
    print('simulation starting...')
elif user_setting.lower() == 'demo':
    for i in range(num_stars):
        star = sphere(pos=vector(random.randrange(-5000, 5000), random.randrange(-5000, 5000),
            random.randrange(-5000, 5000)), mass=random.randrange(100000, 500000), color=color.yellow,
            momentum=vector(random.randrange(-10, 10), random.randrange(-10, 10), random.randrange(-10, 10)),
            make_trail=True, trail_radius=3)
        star.radius = star.mass / 10000
        stars_data.append(star)
        momentum_sum = momentum_sum + star.momentum
    print('simulation starting...')

# ROC of Time
dt = 5000

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
            if i == j:
                continue
            stars_data_j = stars_data[j]
            force = force + cal_force(stars_data_i, stars_data_j)
        stars_data_i.momentum = (stars_data_i.momentum + (force * dt))
        for star in stars_data:
            if star == None:
                continue
            star.pos = (star.pos + (star.momentum * (dt / star.mass)))

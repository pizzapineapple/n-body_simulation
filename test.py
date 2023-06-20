import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Body import Body
from numpy.linalg import norm

# Create a figure and an axis
fig, ax = plt.subplots()

# Set up the axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)


# INverse square law
def det_accel(object_1:Body, object_2:Body) :
    return (object_2.pos-object_1.pos)*100*object_2.mass/(norm(object_1.pos - object_2.pos))**2

body_array = [Body([0,5], [0,0], 1), Body([0,0], [0,0], 1), Body([5,0], [0,0], 1)]

circ_array = []
for i in body_array: 
    circ_array.append(plt.Circle(tuple(i.pos), 0.5))

dt =0.1

# Function to update the animation frame
def update(frame):

    # Apply inverse square law
    for i in body_array:
        for j in body_array:
            if i == j: continue
            accel = det_accel(i,j)
            vel = accel *dt 
            pos = accel * (dt**2 /2)
            # print(pos, vel)
            i.update(pos, vel )

    # Move the circle to a new position
    for ic , i in enumerate(circ_array): i.center = tuple(body_array[ic].pos)
    return circ_array

# Function to initialize the animation
def init():
    # Add the circle to the axis
    for i in circ_array:

        ax.add_patch(i)
    return circ_array

# Create the animation
animation = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=10/dt)

# Display the animation
plt.show()

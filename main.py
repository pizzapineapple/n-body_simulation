import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Body import Body
from numpy.linalg import norm

# Create a figure and an axis
fig, ax = plt.subplots()

# Set up the axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create a circle patch
# circle = plt.Circle((5, 5), 0.5)

# INverse square law
def det_accel(object_1:Body, object_2:Body) :
    return object_2.mass/(norm(object_1.pos - object_2.pos))**2


body_array = [Body([0,0], [0,0], 1), Body([1,0], [0,0], 1)]
circle_arr = [plt.Circle((1,1), 1) for i in body_array ]
# print(circle_arr)
circ = plt.Circle((1,1), 1)

dt = 0.1
# Function to update the animation frame
def update(frame):
    # Apply inverse square law
    # for i in body_array:
    #     for j in body_array:
    #         if i == j: continue
    #         accel = det_accel(i,j)
    #         vel = accel *dt 
    #         pos = accel * (dt**2 /2)
    #         i.update(pos, vel )


    # Move the circle to a new position
    # for i in body_array:
    #     circle_arr.append(circle.center([i.pos]))

    print('update')
    circ.center = (frame % 10, 5)
    return circ,

# Function to initialize the animation
def init():
    print("init")
    # for i in circle_arr:
    #     ax.add_patch(i)
    ax.add_patch(circ)
    return circ

# Create the animation
animation = FuncAnimation(fig, update, frames=100, init_func=init, blit=True)
# Display the animation
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation

x = [0, 1, 2]
y = [0, 1, 2]
yaw = [0.0, 0.5, 1.3]
lims = [0, 10]
fig = plt.figure()
plt.axis('equal')
ax = fig.add_subplot(111)

defaultBox = patches.Rectangle((1, 0), 2, 2, fc='y')
moveBox = patches.Rectangle((0, 0), 5, 5, fc='y')

def init():
    ax.add_patch(defaultBox, moveBox)
    return defaultBox, moveBox,

def animate(i):
    moveBox.set_width(5)
    moveBox.set_height(5)
    moveBox.set_x(x[i])
    # patch._angle = -np.rad2deg(yaw[i])
    return defaultBox, moveBox,

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=len(x),
                               interval=50,
                               blit=True)
plt.xlim(lims)
plt.ylim(lims)
plt.show()
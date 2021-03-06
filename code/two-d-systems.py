#! /usr/bin/python3

# Visualize and solve systems of linear equations in 2d and 3d

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Optional: change default color cycle (requires a recent version of matplotlib)
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=["#377eb8","#ff7f00", "#4daf4a", 
                                                    "#e41a1c", "#984ea3", "#a65628"]) 

## Demo 1: Row picture
# 2x - y = 1 => y = 2x - 1
# x + y = 5 => y = 5 - x
# where do these lines intersect?

# generate points
x = np.array([-5, 5]) # We need only 2 points to draw a line
y1 = 2*x - 1
y2 = 5 - x

# create new figure
plt.figure(figsize=(4, 4), facecolor="w")
# plot the lines
plt.plot(x, y1, x, y2)
# show intersection point
plt.plot(2, 3, "ro", mec="r") 
# add labels and gridlines
plt.title("2d row picture")
plt.xlabel("x")
plt.ylabel("y", rotation=0)
plt.xlim(x)
plt.ylim(ymin=-10)
plt.grid(True)
# uncomment next line to save plot
#plt.savefig("figures/2d-row-picture.png", dpi=150)

## Demo 2: Column picture
# what is the correct linear combination of the column vectors [2 1] and [-1 1] to 
# get the column vector [1 5]?
v1 = np.array([2, 1])
v2 = np.array([-1, 1])
lc = 2*v1 + 3*v2

# uncomment next line to create a new figure. 
#plt.figure(figsize=(4, 4), facecolor="w")
plt.clf()
plt.arrow(0, 0, v1[0], v1[1], color="#377eb8")
plt.arrow(0, 0, v2[0], v2[1], color="#ff7f00")
plt.arrow(0, 0, lc[0], lc[1], color="#e41a1c")
# add title labels, etc.
plt.title("2d column picture")
plt.text(2.1, 1.1, r"$v_1$", color="#377eb8")
plt.text(-1.3, 1.1, r"$v_2$", color="#ff7f00")
plt.text(1.1, 5.1, r"$2 v_1 + 3 v_2$", color="#e41a1c")
plt.xlim((-3, 3))
plt.ylim((-0.5, 5.5))
plt.grid(True)
# uncomment next line to save plot
#plt.savefig("figures/2d-column-picture.png", dpi=150)

# Demo 3: Visualizing how the column space of a 2-by-2 matrix spans the 2d plane
v1 = np.array([2, 1])
v2 = np.array([-1, 1])
a = np.column_stack((v1, v2))
xvals = np.linspace(-3, 3, 31)
yvals = np.linspace(-3, 3, 31)
grid = np.column_stack([[x, y] for x in xvals for y in yvals])
lc = np.dot(a, grid)

# plot linear combinations
# uncomment next line to create a new figure. 
#plt.figure(figsize=(4, 4), facecolor="w")
plt.clf()
plt.plot(lc[0], lc[1], ".", color="#4daf4a", ms=2)
plt.arrow(0, 0, v1[0], v1[1], color="#377eb8", lw=2)
plt.arrow(0, 0, v2[0], v2[1], color="#ff7f00", lw=2)
plt.text(2.5, 1.1, r"$v_1$", color="#377eb8")
plt.text(-2.5, 1.1, r"$v_2$", color="#ff7f00")
plt.title("Column space visualization")
# uncomment below to save plot
#plt.savefig("figures/2d-column-space.png", dpi=150)

# Demo 4: Solving the linear system
# Solve for 1 linear combination
b = np.array([1, 5])
sol = np.linalg.solve(a, b)
print(sol)

# Solve for many linear combinations
sol = np.linalg.solve(a, lc)


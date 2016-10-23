#! /usr/bin/python3

# Visualize and solve systems of linear equations in 2d and 3d

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Optional: change default color cycle (requires a recent version of matplotlib)
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=["#377eb8","#ff7f00", "#4daf4a", 
                                                    "#e41a1c", "#984ea3", "#a65628"]) 

## Demo 1: Row picture
# 2x - y = 1
# x + y = 5

# generate points
x = np.array([-5, 5]) # We need only 2 points to draw a line
y1 = 2*x - 1
y2 = 5 - x

# plot the lines
plt.figure(figsize=(4, 4), facecolor="w", )
plt.plot(x, y1, x, y2)
# show intersection point
plt.plot(2, 3, "ro", mec="r") 
# add labels and gridlines
plt.xlabel("x")
plt.ylabel("y", rotation=0)
plt.xlim(x)
plt.ylim(ymin=-10)
plt.grid(True)

## Demo 2: Column picture
v1 = np.array([2, 1])
v2 = np.array([-1, 1])
lc = 2*v1 + 3*v2

plt.figure(figsize=(4, 4), facecolor="w", )
plt.arrow(0, 0, v1[0], v1[1], color="#377eb8")
plt.arrow(0, 0, v2[0], v2[1], color="#ff7f00")
plt.arrow(0, 0, lc[0], lc[1], color="#e41a1c")

plt.xlabel("x")
plt.ylabel("y", rotation=0)
plt.xlim((-3, 3))
plt.ylim((-0.5, 5.5))
plt.grid(True)

# Demo 3: Visualizing linear combinations
xvals = np.linspace(-3, 3, 31)
yvals = np.linspace(-3, 3, 31)
grid = np.column_stack([[x, y] for x in xvals for y in yvals])
a = np.column_stack((v1, v2))
lc = np.dot(a, grid)

# Plot linear combinations
plt.figure(figsize=(4, 4), facecolor="w", )
plt.plot(lc[0], lc[1], ".", color="#4daf4a", ms=4)
plt.arrow(0, 0, v1[0], v1[1], color="#377eb8", lw=2)
plt.arrow(0, 0, v2[0], v2[1], color="#ff7f00", lw=2)

# Demo 4: Solving the linear system
# Solve for 1 linear combination
b = np.array([1, 5])
sol = np.linalg.solve(a, b)
print(sol)

# Solve for many linear combinations
sol = np.linalg.solve(a, lc)


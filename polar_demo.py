"""
==========
Polar Demo
==========

Demo of a line plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt


r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rticks([0.5,2])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()

#############################################################################
#
# ------------
#
# References
# """"""""""
#
# The use of the following functions, methods, classes and modules is shown
# in this example:

import matplotlib
matplotlib.axes.Axes.plot
matplotlib.projections.polar
matplotlib.projections.polar.PolarAxes
matplotlib.projections.polar.PolarAxes.set_rticks
matplotlib.projections.polar.PolarAxes.set_rmax
matplotlib.projections.polar.PolarAxes.set_rlabel_position

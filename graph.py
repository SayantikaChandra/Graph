import matplotlib.pyplot as pt
import numpy as name

# evenly sampled time at 200ms intervals
t = name.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
pt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
pt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 17:51:05 2020

@author: Micha
"""
import time as tm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style

style.use('bmh')


x_data = []
y_data = []



distance_values = []
i = 0
while i < 10:
    distance_values.append(i)
    i += 1
while i > 0:
    distance_values.append(i)
    i -= 1
size = len(distance_values)+1
time = list(range(0, size))


tm.sleep(3)
fig, ax = plt.subplots()
ax.set_xlim(0,size)
ax.set_ylim(0,4.5)
line, = ax.plot(0,0)

def animation_frame(i):
    x_data.append(time[i])
    y_data.append(distance_values[i])
    
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    line.set_linewidth(7)
    line.set_color('black')
    return line,


animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(1, size, 1), interval=300)
plt.axhline(y=1, color='black', label="Grenzwert", linewidth=4, linestyle='--')
plt.fill_between(list(range(0,size+1)), 1, color='red')
#plt.fill_between(list(range(0,size+1)), 0.5, color='red')
plt.xlabel('Zeit')
plt.ylabel('Distanz [m]')
plt.legend(loc='upper left')
plt.show()






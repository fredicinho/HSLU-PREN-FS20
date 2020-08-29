# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 21:01:31 2020

@author: Micha
"""

import matplotlib.pyplot as plt
import numpy as np

# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')



def live_plotter(x_vec,y1_data,y2_data,y3_data,line1, line2, line3, identifier='',pause_time=0.08):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig, axs = plt.subplots(3, 1)
     #   ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = axs[0].plot(x_vec, y1_data, alpha=0.8, color="black")
        line2, = axs[1].plot(x_vec, y2_data, alpha=0.8, color="black")
        line3, = axs[2].plot(x_vec, y3_data, alpha=0.8, color="black")




        #update plot label/title
        axs[0].set_ylabel('TOF1 - Right')
        axs[1].set_ylabel('TOF2 - Left')
        axs[2].set_ylabel('TOF3 - Pylone')
        axs[2].set_xlabel('time [s]')
        axs[0].set_ylim(-10,1700)
        axs[1].set_ylim(-10,1700)
        axs[2].set_ylim(-10,1700)
        axs[0].axhline(y=1000, color='red', label="Grenzwert", linewidth=1, linestyle='--')
        axs[1].axhline(y=1000, color='red', linewidth=1, linestyle='--')
        axs[2].axhline(y=200, color='red', linewidth=1, linestyle='--')


        fig.suptitle('Distanzmessung in [mm]', fontsize=16)
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    line2.set_ydata(y2_data)
    line3.set_ydata(y3_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1, line2, line3




# the function below is for updating both x and y values (great for updating dates on the x-axis)
def live_plotter_xy(x_vec,y1_data,line1,identifier='',pause_time=0.01):
    if line1==[]:
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        line1, = ax.plot(x_vec,y1_data,'r-o',alpha=0.8)
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
        
    line1.set_data(x_vec,y1_data)
    plt.xlim(np.min(x_vec),np.max(x_vec))
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])

    plt.pause(pause_time)
    
    return line1
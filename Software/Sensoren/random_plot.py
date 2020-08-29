# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:35:15 2020

@author: Micha
"""

from pylive import live_plotter
import numpy as np

tof12_max = 1600
tof3_max = 1600
TIME_INTERVALL = np.arange(0, 30, 1)

TOF1_FRONT_RIGHT = [tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,  #0 - 2s
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,  #2.2 - 4s
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,  #4.2 - 6s
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,  #6.2 - 8s
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,  #8.2 - 10s
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,  #10.2 - 12s
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,  #12.2 - 14s
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,  #14.2 - 16s
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,  #16.2 - 18s
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,  #18.2 - 20s
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,  #20.2 - 22s
                    1500, 1450, 1400, 1350, 1300, 1250, 1110, 1000, 950, 900,  #22.2 - 24s
                    850, 780, 600, 440, 280, 270, 260, 240, 230, 210,  #24.2 - 26s
                    180, 150, 140, 130, 120, 100, 75, 50, tof12_max, tof12_max,  #26.2 - 28s
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                    tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max]

TOF2_FRONT_LEFT = [tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, 1600, 1550, 1450, 1350, 1250, 1200, 1140, 1050,
                   1000, 750, 525, 400, 250, 250, 240, 220, 220, 210,
                   180, 150, 140, 130, 120, 100, 75, 50, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max,
                   tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max, tof12_max]

TOF3_PYLONE = [tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, 550, 550, 550, 550, 550, 530, 510, 500, 480,
               440, 400, 350, 300, 280, 270, 250, 240, 230, 220,
               200, 195, 190, 170, 170, 170, 150, 130, 120, 120,
               100, 100, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               1000, 950, 850, 800, 700, 650, 600, 550, 550, 550,
               550, 550, 550, 550, 530, 500, 450, 350, 300, 250,
               210, 200, 190, 170, 150, 140, 110, 100, 100, 100,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max,
               tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max, tof3_max]

size = 40  #Anzahl Punkt auf Plot
x_vec = np.linspace(-8,0,size+1)[0:-1]

y_vec1, y_vec2, y_vec3 = np.zeros(len(x_vec)), np.zeros(len(x_vec)), np.zeros(len(x_vec))
line1 = []
line2 = []
line3 = []
while True:
    rand_val = np.random.randn(1)*10
    y_vec1[-1] = TOF1_FRONT_RIGHT.pop(0) + rand_val
    y_vec2[-1] = TOF2_FRONT_LEFT.pop(0) + rand_val
    y_vec3[-1] = TOF3_PYLONE.pop(0) + rand_val

    line1, line2, line3 = live_plotter(x_vec, y_vec1, y_vec2, y_vec3, line1, line2, line3)
    y_vec1 = np.append(y_vec1[1:], 0.0)
    y_vec2 = np.append(y_vec2[1:], 0.0)
    y_vec3 = np.append(y_vec3[1:], 0.0)

    if (not TOF1_FRONT_RIGHT):
        break
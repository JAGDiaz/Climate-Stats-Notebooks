#! /usr/bin/python3

import numpy as np

def Summary(x):
    deets = np.quantile(x, [0, .25, .5, .75, 1])
    print("Min     1st Qu. Median  3rd Qu.  Max")
    print(f"{deets[0]:4.4f} {deets[1]:4.4f} {deets[2]:4.4f} {deets[3]:4.4f} {deets[4]:4.4f}")

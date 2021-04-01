import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, to_rgba


def newColMap(colors):
    first = np.repeat([to_rgba(colors[0])], 4, axis = 0)
    last = np.repeat([to_rgba(colors[-1])], 4, axis = 0)
    v = cm.get_cmap('viridis', 16*(len(colors)-2))
    newcolors = v(np.linspace(0, 1, 16*(len(colors)-2)))
    for (i, col) in enumerate(colors[1:-1]):
        newcolors[16*i : 16*(i+1), :] = to_rgba(col)
    return ListedColormap(np.append(np.append(first,newcolors, axis=0), last, axis=0))

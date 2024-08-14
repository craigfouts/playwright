import matplotlib.pyplot as plt
import numpy as np

def plot(x, size=10, color='white', edgecolors='none', opacity=1., winsize=100, facecolor='black'):
    plt.tight_layout()
    fig, ax = plt.subplots(1, 1, facecolor=facecolor, constrained_layout=True)
    ax.scatter(*x.T, s=size, c=color, edgecolors=edgecolors, alpha=opacity)
    ax.axis([0, winsize, 0, winsize])
    ax.invert_yaxis()
    ax.set_axis_off()
    return fig

def grab_plot(close=True):
    fig = plt.gcf()
    fig.canvas.draw()
    img = np.array(fig.canvas.renderer._renderer)
    a = np.float32(img[..., 3:]/255.)
    img = np.uint8(255.*(1. - a) + img[..., :3]*a)
    if close:
        plt.close()
    return img

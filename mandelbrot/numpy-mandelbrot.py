import matplotlib.pyplot as plt
import numpy as np
import math 
from tqdm import tqdm

def next_mandelbrot(z, c):
    return z ** 2 + c
def run_sequence(c, iterations, total=complex(0,0)):
    magnitude = math.sqrt(total.real ** 2 + total.imag ** 2) 
    if magnitude > 2:
        return (False, iterations) 
    elif iterations <= 0:
        return (True, iterations)
    
    return run_sequence(c, iterations-1, total=next_mandelbrot(total, c))

#create the bounds of the mandelbrot set
real_min = -2
real_max = 2
imag_min = -2
imag_max = 2
#create the percision
per = 0.001
iterations = 75

#make the lists for all the x and the y values for the numpy
all_x_vals = []
all_y_vals = []

all_values = np.array([[(i, j) for j in np.arange(imag_min, imag_max, per)] for i in tqdm(np.arange(real_min, real_max, per))])

for i in tqdm(all_values):
    for j in i:
        all_x_vals.append(j[0])
        all_y_vals.append(j[1])
color = []

for i in tqdm(np.arange(real_min, real_max, per)):
    color_row = []
    for j in np.arange(imag_min, imag_max, per):
        inital_c_value = complex(i, j)
        result = run_sequence(c=inital_c_value, iterations=iterations)
        if result[0]:
            color_row.append([0,0,0])
        else:
            faulty_iteration = (iterations - result[1])/iterations
            to_rgb = faulty_iteration * 255
            color_row.append([255-to_rgb,to_rgb,255-to_rgb])
    color.append(color_row)
fig, ax = plt.subplots()

numpy_color = np.array(color)
formatted_color = numpy_color.reshape(-1, 3) / 255

ax.scatter(all_x_vals, all_y_vals, c=formatted_color)
ax.set(xlim=(real_min, real_max), xticks=np.arange(real_min, real_max),
     ylim=(imag_min, imag_max), yticks=np.arange(imag_min, imag_max))

plt.show()

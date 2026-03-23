Web VPython 3.2


black = color.black

#craft the graph
mandelbrot_graph = graph(title="Mandelbrot", ytitle="Complex Numbers", xtitle="Real Numbers")
#make a dots category for dots that are found in the mandelbrot set
mandelbrot_dots = gdots(graph=mandelbrot_graph, color=black)
non_mandelbrot_dots = gdots(graph=mandelbrot_graph, color=color.red)

#real max and min
real_max = 2
real_min = -2

#complex-max and min
imagine_max = 2
imagine_min = -2

#percision
per = 0.2

class Complex:
    def __init__(self, real, complex):
        self.real = real
        self.complex = complex
    def multiply(self, value):
        #value must be complex
        a = self.real * value.real
        b = self.real * value.complex
        c = self.complex * value.real
        d = self.complex * value.complex * -1
        
        return Complex(a+d, b+c)
        
#find the next value in the mandelbrot set given a certain z and c value.
def mandelbrot_next(z, c):
    return z ** 2 + c
#recursive sequence to iterate through mandelbrot set, total amount of times
def iterate_mandelbrot(z=0, c=0, max_iterations=0):
    if z > 2:
        return True 
    elif max_iterations <= 0:
        return False
    
    print(mandelbrot_next(z,c))
    return iterate_mandelbrot(mandelbrot_next(z,c), c, max_iterations - 1)

for i in range(real_min, real_max, per):
    for j in range(imagine_min, imagine_max, per):
        inital_c_val = i + j * sqrt(-1)
        in_mandelbrot = iterate_mandelbrot(0, inital_c_val, 10)
        
        if in_mandelbrot:
            mandelbrot_dots.plot(i, j)
        else:
            non_mandelbrot_dots.plot(i,j)
            

        

Web VPython 3.2

#Make the class complex which stores all the numbers
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def add(self, c):
        sum_real = self.real + c.real
        sum_imaginary = self.imaginary + c.imaginary
        return Complex(sum_real, sum_imaginary)
    
    def multiply(self, c):
        q = self.real * c.real
        w = self.real * c.imaginary
        e = self.imaginary * c.real
        r = self.imaginary * c.imaginary  * -1
        
        sum_real = q + r
        sum_imaginary = w + e
        return Complex(sum_real, sum_imaginary)
    
    def exponiate(self, n, current=0):
        if n <= 0:
            return current
        return exponiate(n-1, current=self.multiply(self))

black = color.black

#percision
per = 0.01
total_iterations = 75

#craft the graph
mandelbrot_graph = graph(title="Mandelbrot", ytitle="Complex Numbers", xtitle="Real Numbers", height=640)
#make a dots category for dots that are found in the mandelbrot set
mandelbrot_dots = gdots(graph=mandelbrot_graph, color=black, radius=per*50)
non_mandelbrot_dots = gdots(graph=mandelbrot_graph, color=color.red, radius=per * 50)

#real max and min
real_max = 0.5
real_min = -2

#complex-max and min
imagine_max = 1
imagine_min = -1


#find the next value in the mandelbrot set given a certain z and c value.
def mandelbrot_next(z, c):
    return c.add(z.exponiate(2))
#recursive sequence to iterate through mandelbrot set, total amount of times
def iterate_mandelbrot(z, c, max_iterations=0):
    if z.real > 2:
        return (False, max_iterations)
    elif max_iterations <= 0:
        return (True, 0)
    
    return iterate_mandelbrot(mandelbrot_next(z,c), c, max_iterations - 1)


for i in range(real_min, real_max, per):
    for j in range(imagine_min, imagine_max, per):
        inital_c_val = Complex(i, j)
        in_mandelbrot = iterate_mandelbrot(Complex(0,0), inital_c_val, total_iterations)
        
        if in_mandelbrot[0]:
            mandelbrot_dots.plot(i, j)
        else:
            total = total_iterations - in_mandelbrot[1]
            chosen_hue = 1 - total / total_iterations
            chosen_color = vec(chosen_hue, 1, 1)
            set = gdots(graph=mandelbrot_graph, color=color.hsv_to_rgb(chosen_color), radius=per* 50)
            set.plot(i,j)

Web VPython 3.2
#Make the class complex which stores all the numbers
class Complex:
    def __init__(self, real, imaginary):   #
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
    
    def exponentiate(self, n, current=0):
        if n <= 0:
            return current
        return exponentiate(n-1, current=self.multiply(self))

black = color.black

#percision
per = 0.01
total_iterations = 175

#craft the graph
mandelbrot_graph = graph(title="Mandelbrot", ytitle="Complex Numbers", xtitle="Real Numbers", height=640)
#make a dots category for dots that are found in the mandelbrot set
mandelbrot_dots = gdots(graph=mandelbrot_graph, color=black, radius=per*50)
non_mandelbrot_dots = gdots(graph=mandelbrot_graph, color=color.blue, radius=per * 50)
sketch_dots = gdots(graph=mandelbrot_graph, color=color.green, radius=per*50)
#real max and min
real_max = 0.5
real_min = -2

#complex-max and min
imagine_max = 1
imagine_min = -1


#find the next value in the mandelbrot set given a certain z and c value.
def mandelbrot_next(z, c):
    return c.add(z.exponentiate(2))
#recursive sequence to iterate through mandelbrot set, total amount of times

def iterate_loop(c):
    xold=0
    yold=0
    period=0
    z=Complex(0,0)
    i=0
    while i < total_iterations:
        x = z.real
        y = z.imaginary 
        
        z=mandelbrot_next(z, c)
        if x**2+y**2>4:
            return (False,i)
            
        period+=1
        i+=1
        
     #   if (abs(x-xold)<0.0000001 and abs(y-yold)<0.0000001):
     #       return (True,0)
        
        if period==20:
            period=0
            xold=x
            yold=y
            
    
    return (True,0)
            
        
        
            
def pre_check(c):
    x = c.real
    y = c.imaginary
    abs_c_square = x**2+y**2
    side1 = abs_c_square*(8*abs_c_square-3) #bounds of cardiod
    side2 = 3/32-x
    side1c = (x+1)**2 + y**2 #bounds of period 2
    
    if side1<=side2 | side1c<1/16: #1/16, also check if in main cardioid or pd 2
        return (True, 0)
    else:
        return False


for i in range(real_min, real_max, per):
    for j in range(imagine_min+(imagine_max-imagine_min)/2, imagine_max, per):
        rate(100)
        inital_c_val = Complex(i, j)
    
        in_mandelbrot = pre_check(inital_c_val)
        if not in_mandelbrot:
            in_mandelbrot = iterate_loop(inital_c_val)
        
        if in_mandelbrot[0]:
            mandelbrot_dots.plot(i, j)
            if j != 0:
               mandelbrot_dots.plot(i,-j)
        else:
            total = total_iterations - in_mandelbrot[1]
            chosen_hue = 1 - total / total_iterations
            chosen_color = vec(chosen_hue, 1, 1)
            set = gdots(graph=mandelbrot_graph, color=color.hsv_to_rgb(chosen_color), radius=per* 50)
            set.plot(i,j)
            if j != 0:
               set.plot(i,-j)


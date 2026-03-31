Web VPython 3.2
scene.resizabe = False
scene.userzoom = False
scene.userspin = False
scene.userpan = False
scene.autoscale = True 

screen_scale = (100,100)

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
    def magnitude(self):
        return sqrt(self.real ** 2 + self.imaginary * self.imaginary * -1)



class Resolution:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        #auto calculate the center
        self.c = (ceil(self.w/2), ceil(self.h/2))
    
        
class Memory:
    #memory stores value in a grid shape and can expand in multiple directions
    def __init__(self):
        self.memory = []
        
    def add_row(self, r):
        #expects a row
        self.memory.append(r)
    def pop_row(self, i):
        #remove a row from memory
        self.memory.pop(i)
        
    def add_column(self, c):
        if len(c) == len(self.memory):
            for i in range(len(c)):
                self.memory[i].append(c[i])
    def set_value(self, coor, v):
        self.memory[coor[0]][coor[1]] = v
        
    def get_value(self, coor):
        return self.memory[coor[0]][coor[1]]
    

class Screen:
    def __init__(self, resolution):
        self.resolution = resolution
        self.memory = Memory()
        
        #Locks redimensioning of screen
        self.hasloaded = False
    def in_screen(self, coor):
        xcoors = (ceil(-1 * self.resolution.w/2), ceil(self.resolution.w/2))
        ycoors = (ceil(-1 * self.resolution.h/2), ceil(self.resolution.h/2))     
        return ((xcoors[0] < coor[0] < xcoors[1]) and (ycoors[0] < coor[1] < ycoors[1]))
    def render(self):
        #Make sure that the aspect ratio did not change unexpectedially
        if not self.hasloaded:
            for i in range(self.resolution.w):
                rate(100000)
                pixel_array = []
                for j in range(self.resolution.h):
                    xpos = i - self.resolution.w/2
                    ypos = j - self.resolution.h/2
                    position = vec(xpos, ypos, 0)
                    dimensions=vec(1,1,1)
                    emissive=True
                    box_color = vec(i/self.resolution.w, j/self.resolution.h, 1)
                    pixel = box(pos=position, size=dimensions, color=box_color, emissive=emissive)
                    pixel_array.append(pixel)
                #add value to memory for future use
                self.memory.add_row(pixel_array)
            #Prevent redimensioning of the screen
            self.hasloaded = True
    
    def render_values(self, cm):
        #render all new color values from color matrix
        for i in range(self.resolution.w):
            rate(1000)
            for j in range(self.resolution.h):
                self.memory.get_value((i,j)).color = cm[i][j]
    
    def change_value(self, coor, c):
        self.memory.get_value((coor[0], coor[1])).color = c
                

#find the next value in the mandelbrot set given a certain z and c value.
def mandelbrot_next(z, c):
    return c.add(z.exponiate(2))
#recursive sequence to iterate through mandelbrot set, total amount of times
def iterate_mandelbrot(z, c, max_iterations=100):
    if z.magnitude() > 2:
        return (False, max_iterations)
    elif max_iterations <= 0:
        return (True, 0)
    
    return iterate_mandelbrot(mandelbrot_next(z,c), c, max_iterations - 1)
        
   
#Render the screen properly 
res = Resolution(50, 50)
pixels = Screen(res)
pixels.render()



#Load mandelbrot
wt = wtext(text="Loading")

#iterate through i and j
for i in range(res.w):
    rate(10000)
    
    calc = ceil(i/res.w * 10)
    hashtags = "".join("#" for i in range(calc))
    wt.text = f"{int(i / res.w * 100)}% [{hashtags}]"
    
    for j in range(res.h):
        xcor = ((i - res.c[0])/(res.c[0]))*2
        ycor = ((j - res.c[1])/(res.c[1]))*2
        complex_num = Complex(xcor, ycor)
        maddie = iterate_mandelbrot(z=Complex(0,0), c=complex_num, max_iterations=100) 
        if maddie[0]:
            pixels.change_value((i,j), vec(0,0,0))
        else:
            c = vec(maddie[1]/100, 1-maddie[1]/100, 2*maddie[1]/100)
            pixels.change_value((i,j), c)
wt.text = ""


#magnificatio
magnification = 0.2

#Zoom into a certain area
while True:
        rate(30)
        
        #Get the mouse coordinates
        myevt = scene.waitfor('click')
        mpos = scene.mouse.project(point=vec(0,2,0), normal=vec(0,0,1))
        if mpos:
            if pixels.in_screen((mpos.x, mpos.y)):
                
            
            
        





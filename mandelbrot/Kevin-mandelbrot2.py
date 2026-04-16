GlowScript 3.2 VPython
#starting parameters

scene.delete()
startX = 0
startY = 0
startMag = 1
#slider setup
scene.caption = ""
scene.append_to_caption("\nHere is a graph:\n")
Xslider = slider(bind = createX, min = -2.5, max = 2.5, value = 0, step = .1, disabled = True)
scene.append_to_caption("X-Coordinate Center: ")
sx = wtext(text = '{:1.1f}'.format(startX)+"\n")
Yslider = slider(bind = createY, min = -2.5, max = 2.5, value = 0, step = .1, disabled = True)
scene.append_to_caption("Y-Coordinate Center: ")
sy = wtext(text = '{:1.1f}'.format(startY)+"\n")
Magslider = slider(bind = createMag, min = .1, max = 20, value = 1, step = .10, disabled = True)
scene.append_to_caption("Magnification: ")
smag = wtext(text = '{:1.0f}'.format(startMag*100)+"%\n")
scene.delete()
setg = graph(title = "Mandelbrot Set", xtitle = "Real", ytitle = "Imaginary", xmax =startX+(2.0)/startMag, xmin = startX+(-2.0)/startMag, ymax = startY+(2.0)/startMag, ymin = startY+(-2.0)/startMag, height  = 650, width = 650)
#Basic float-only version
#functions called when adjusting sliders

def createX(evt):
    #console.log(evt)

    global startX
    startX = Xslider.value #variable update
    global sx
    sx.text = '{:1.1f}'.format(startX)+"\n" #wtext update   
    reset()

def reset():
    toggle(True)
    global setg #deletes then recreates mandelbrot graph
    setg.delete()
    global running
    setg = graph(title = "Mandelbrot Set", xtitle = "Real", ytitle = "Imaginary", xmax =startX+(2.0)/startMag, xmin = startX+(-2.0)/startMag, ymax = startY+(2.0)/startMag, ymin = startY+(-2.0)/startMag, height  = 650, width = 650)
    iteration()
    toggle(False)
    
def createY(evt):
    #console.log(evt)
    global startY
    startY = Yslider.value
    global sy
    sy.text= '{:1.1f}'.format(startY)+"\n"

    reset()

def createMag(evt):
    #console.log(evt)
    global startMag
    startMag = Magslider.value
    global smag
    smag.text = '{:1.0f}'.format(startMag*100)+"%"+"\n"

    reset()

def iteration():
        for r in range(startX+(-2.0)/startMag,startX+(2.0)/startMag, .02/startMag):   #iterates along the real values; -2, .5 range due to reference: sci-pi.org.uk/mandel/mandel_vs_log.html 
            
            min = startY+(-2.0)/startMag
            max = startY+(2.0)/startMag
            arr = check_symmetry(startY,startMag)
            if arr != False:
                min = arr[0]
                max = arr[1]
                symMax = arr[3]
            for i in range(min, max+.01/startMag, .02/startMag): #iterates along the imaginary values
                
                rate(1000000*startMag) #<- procedurally loads the graph by sections
                #TAKES ~2 SECONDS FOR -2,.5,.01; -2,2,.01; N=500 steps
                cZr = r #current Z real component starts at real value r
                cZi = i #current Z imaginary component starts at imaginary value i
                cZr_new = r #creates a placeholder real component used while iterating currentZ values
                send = True
                iter = 0
                if pre_check(r, i) == False:
                    for N in range(1000): #iterates current Z imaginary and real components according to Znew = Zcurr**2+Zorig
                        cZr_new = cZr*cZr-cZi*cZi+r #placeholder holds iterated real Z component from equation Znew = Zcurr**2+Zorig
                        cZi = cZr*cZi*2+i #imaginary Z component from equation Znew = Zcurr**2+Zorig
                        cZr = cZr_new #Sets current real Z component equal to the placeholder real component
                        if cZr*cZr+cZi*cZi > 4: #checks for validity 
                            send = False
                            iter = N
                            break
                absi = abs(i)
                if send: #adds to plot if the magnitude of the points is less than 2
                    gdots(graph = setg, color = color.red, radius = 1).plot(r, i) #plots points; each dot has a radius of .3 
                    if absi != 0 and symMax > absi:
                        gdots(graph = setg, color = color.red, radius = 1).plot(r, -i)
                else:
                    gdots(graph = setg, color = vec(iter/512, iter/32, iter/8), radius = 1).plot(r,i)
                    if absi != 0 and symMax > absi:
                        gdots(graph = setg, color = vec(iter/512, iter/32, iter/8), radius = 1).plot(r,-i)

def toggle(bool):
   Xslider.disabled = bool
   Yslider.disabled = bool
   Magslider.disabled = bool

toggle(True)
iteration()
toggle(False)


def pre_check(x,y): #real and imaginary
    abs_c_square = x**2+y**2
    side1 = abs_c_square*(8*abs_c_square-3) #bounds of cardiod
    side2 = 3/32-x
    side1c = (x+1)**2 + y**2 #bounds of period 2
    
    if side1<=side2 or side1c<1/16: #1/16, also check if in main cardioid or pd 2
        return True
    else:
        return False

def check_symmetry(startY, startMag):
    min = startY-(2.0)/startMag
    max = startY+(2.0)/startMag
    if min > 0 and max > 0 or min < 0 and max < 0:
        return False
    #else if max + min < 0:
    #    return [min, 0, 0, max] #first pair indicates iteration range
    else: 
        return [0, max, 0, abs(min)]  #second pair is the range to apply symmetry





#Graph takes 1 min ~50 seconds for -2, .5, .001; -2, 2, .001; N=1000 steps

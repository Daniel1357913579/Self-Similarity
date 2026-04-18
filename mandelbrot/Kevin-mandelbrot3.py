GlowScript 3.2 VPython
#starting parameters
running = True

hairLen=0.2

def crossHair():
    global hair
    global crossH
    if crossH:
        hair.delete()
        crossH=False
        return
    hair = gdots(graph = setg, color = color.green, radius = 1)
    iX=startX
    iY=startY
    hair.plot(iX,iY)
    i=0.02/startMag
    while i < hairLen:
        hair.plot(iX+i,iY)
        hair.plot(iX-i,iY)
        hair.plot(iX,iY+i)
        hair.plot(iX,iY-i)
        i+=0.02/startMag
        
    crossH=True


scene.bind('keydown', key_pressed)

def key_pressed(evt):
    global so, hairLen, startX, startY, startMag
    k = evt.key
    if k == 'q' and hairLen > 0.2:
        hairLen-=0.2
        so.text = ' {:1.1f}'.format(hairLen)+"\n"
    if k == 'w' and hairLen < 1:
        hairLen+=0.2
        so.text = ' {:1.1f}'.format(hairLen)+"\n"
    if running:
        return
    if k == 'up':
        startY +=  hairLen
        reset()
        print("done")
    elif k == 'down':
        startY -=  hairLen
        reset()
        print("done")
    elif k == 'left':
        startX -=  hairLen
        sx = wtext(text = '{:1.1f}'.format(startX)+"\n")
        reset()
        print("done")
    elif k == 'right':
       startX +=  hairLen
       reset()
       print("done")
    elif k == '1':
       startMag -= 0.5
       reset()
       print("done")
    elif k == '2':
       startMag += 0.5
       reset()
       print("done")

startX = 0
startY = 0
startMag = 1


scene.caption = "" 
scene.append_to_caption("\nHere is a graph:\n - Press 1 to zoom out, 2 to zoom in\n - Use arrows to shift center\n")
 
but = button(bind = crossHair, text = 'Crosshair Toggle. Use Q(-) and W(+) to change size')
so = wtext(text = ' {:1.1f}'.format(hairLen)+"\n")

scene.append_to_caption("\nX-Coordinate Center: ")
sx = wtext(text = '{:1.1f}'.format(startX)+"\n")

scene.append_to_caption("Y-Coordinate Center: ")
sy = wtext(text = '{:1.1f}'.format(startY)+"\n")

scene.append_to_caption("Magnification: ")
smag = wtext(text = '{:1.0f}'.format(startMag*100)+"%\n")
scene.delete()
setg = graph(title = "Mandelbrot Set", xtitle = "Real", ytitle = "Imaginary", xmax =startX+(2.0)/startMag, xmin = startX+(-2.0)/startMag, ymax = startY+(2.0)/startMag, ymin = startY+(-2.0)/startMag, height  = 650, width = 650)
#Basic float-only version
#functions called when adjusting sliders
hair=gdots(graph = setg, color = color.green, radius = 1)
crossH=False


def reset():  
    sx.text='{:1.1f}'.format(startX)+"\n"
    sy.text='{:1.1f}'.format(startY)+"\n"
    smag.text='{:1.0f}'.format(startMag*100)+"%\n"
    global running
    rate(1000)
    global setg #deletes then recreates mandelbrot graph
    setg.delete()
    setg = graph(title = "Mandelbrot Set", xtitle = "Real", ytitle = "Imaginary", xmax =startX+(2.0)/startMag, xmin = startX+(-2.0)/startMag, ymax = startY+(2.0)/startMag, ymin = startY+(-2.0)/startMag, height  = 650, width = 650)
    running = True
    iteration()
    running = False

def iteration():
        for r in range(startX+(-2.0)/startMag,startX+(2.0)/startMag, .02/startMag):   #iterates along the real values; -2, .5 range due to reference: sci-pi.org.uk/mandel/mandel_vs_log.html         
            min = startY+(-2.0)/startMag
            max = startY+(2.0)/startMag
            increment = 0.02/startMag
            arr = check_symmetry(startY,startMag)
            if arr != False:
                limit = arr[0]
                symMax = arr[2]
                increment = increment*arr[1] 
                iterateSym(r,symMax,limit,increment)
            else:
                iterateNormal(r,min,max,increment)

def iterateNormal(r,min, max, increment):
    i=min
    while i <= max: #iterates along the imaginary values
        if not running:
            return
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
        if send: #adds to plot if the magnitude of the points is less than 2
            gdots(graph = setg, color = color.red, radius = 1).plot(r, i) #plots points; each dot has a radius of .3 
        else:
            gdots(graph = setg, color = vec(iter/512, iter/32, iter/8), radius = 1).plot(r,i)
    
        i = i+increment
    
def iterateSym(r,symMax,max, increment):
    i=0
    while abs(i) <= max: #iterates along the imaginary values
        if not running:
            return
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
    
        i = i+increment

iteration()
running = False


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
    else if max + min < 0:
        return [abs(min), -1, max] 
    else: 
        return [max, 1, abs(min)]  





#Graph takes 1 min ~50 seconds for -2, .5, .001; -2, 2, .001; N=1000 steps

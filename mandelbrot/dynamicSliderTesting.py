Web VPython 3.2
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
##Basic List Version
#def modulus(v):
#    #the v[0] component is the real component, the v[1] component is the imaginary component
#    return sqrt(v[0]**2+v[1]**2)
#def phase(v):
#    return atan2(v[1], v[0])
#def conjugate(v):
#    return [v[0], -1*v[1]]
#def prtstr(v):
#    print(v[0], "i:", v[1])
#def add(v, b):
#    return [v[0] + b[0], v[1]+b[1]]
#def sub(v, b):
#    return[v[0]-b[0],v[1]-b[1]]
#def mult(v, b):
#    return[v[0]*b[0]-v[1]*b[1], v[0]*b[1]+v[1]*b[0]]
#def div(v, b):
#    return(mult(mult(v, conjugate(b)), [modulus(b), 0]))
#
#set = graph(title = "Mandelbrot Set", xtitle = "Real", ytitle = "Imaginary")
#
#origZ = [0,0]
#currZ = [0,0]
#def newCurr():
#    global currZ  
#    #currZ = add(mult(currZ, currZ), origZ) 
#    #takes 15 seconds on -2,.5,.01; -2,2,.01; N=500 steps
#    
#    #takes 8 seconds on -2,.5,.01; -2,2,.01; N=500 steps
#
#for r in range(-2, .5, 0.001):
#    for i in range(-2, 2, 0.01):
#        origZ[0] = r
#        origZ[1] = i
#        currZ[0] = r
#        currZ[1] = i
#        for N in range(500):
#            currZ = [currZ[0]*currZ[0]-currZ[1]*currZ[1]+origZ[0], currZ[0]*currZ[1]*2+origZ[1]] 
#        if modulus(currZ) < 2:
#            gdots(graph = set, color = color.red).plot(r, i)
#            
#        
#Basic float-only version
#functions called when adjusting sliders
def createX(evt):
    console.log(evt)
    global startX
    startX = evt.value #variable update
    global sx
    sx.text = '{:1.1f}'.format(startX)+"\n" #wtext update
    global setg #deletes then recreates mandelbrot graph
    setg.delete()
    setg = graph(title = "Mandelbrot Set", xtitle = "Real", ytitle = "Imaginary", xmax =startX+(2.0)/startMag, xmin = startX+(-2.0)/startMag, ymax = startY+(2.0)/startMag, ymin = startY+(-2.0)/startMag, height  = 650, width = 650)
    for r in range(startX+(-2.0)/startMag,startX+(2.0)/startMag, .02/startMag):   #iterates along the real values; -2, .5 range due to reference: sci-pi.org.uk/mandel/mandel_vs_log.html 
      for i in range(startY+(-2.0)/startMag, startY+(2.0)/startMag, .02/startMag): #iterates along the imaginary values
    
        #TAKES ~2 SECONDS FOR -2,.5,.01; -2,2,.01; N=500 steps
        cZr = r #current Z real component starts at real value r
        cZi = i #current Z imaginary component starts at imaginary value i
        cZr_new = r #creates a placeholder real component used while iterating currentZ values
        send = True
        iter = 0
        for N in range(1000): #iterates current Z imaginary and real components according to Znew = Zcurr**2+Zorig
            cZr_new = cZr*cZr-cZi*cZi+r #placeholder holds iterated real Z component from equation Znew = Zcurr**2+Zorig
            cZi = cZr*cZi*2+i #imaginary Z component from equation Znew = Zcurr**2+Zorig
            cZr = cZr_new #Sets current real Z component equal to the placeholder real component
            if cZr*cZr+cZi*cZi > 4: #checks for validity 
                send = False
                iter = N
                break
        if send: #adds to plot if the magnitude of the points is less than 2
            gdots(graph = setg, color = color.red, radius = .3).plot(r, i) #plots points; each dot has a radius of .3 
        else:
          gdots(graph = setg, color = vec(iter/512, iter/32, iter/8), radius = .3).plot(r,i)
    global Xslider
    if startMag > 10:
        Xslider.delete()
        Xslider = slider(bind = createX, min = -.25, max = .25, value = 0, step = .01, disabled = True)
    else: 
        Xslider.delete()
        Xslider = slider(bind = createX, min = -2.5, max = 2.5, value = 0, step = .1, disabled = True)
    global Yslider
    if startMag > 10:
        Yslider.delete()
        Yslider  = slider(bind = createY, min = -.25, max = .25, value = 0, step = .01, disabled = True)
    else: 
        Yslider.delete()
        Yslider = slider(bind = createY, min = -2.5, max = 2.5, value = 0, step = .1, disabled = True)
def createY(evt):
    console.log(evt)
    global startY
    startY = evt.value
    global sy
    sy.text= '{:1.1f}'.format(startY)+"\n"

    global setg
    setg.delete()
    setg = graph(title = "Mandelbrot Set", xtitle = "Real", ytitle = "Imaginary", xmax =startX+(2.0)/startMag, xmin = startX+(-2.0)/startMag, ymax = startY+(2.0)/startMag, ymin = startY+(-2.0)/startMag, height  = 650, width = 650)
    for r in range(startX+(-2.0)/startMag,startX+(2.0)/startMag, .02/startMag):   #iterates along the real values; -2, .5 range due to reference: sci-pi.org.uk/mandel/mandel_vs_log.html 
      for i in range(startY+(-2.0)/startMag, startY+(2.0)/startMag, .02/startMag): #iterates along the imaginary values
    
        #TAKES ~2 SECONDS FOR -2,.5,.01; -2,2,.01; N=500 steps
        cZr = r #current Z real component starts at real value r
        cZi = i #current Z imaginary component starts at imaginary value i
        cZr_new = r #creates a placeholder real component used while iterating currentZ values
        send = True
        iter = 0
        for N in range(1000): #iterates current Z imaginary and real components according to Znew = Zcurr**2+Zorig
            cZr_new = cZr*cZr-cZi*cZi+r #placeholder holds iterated real Z component from equation Znew = Zcurr**2+Zorig
            cZi = cZr*cZi*2+i #imaginary Z component from equation Znew = Zcurr**2+Zorig
            cZr = cZr_new #Sets current real Z component equal to the placeholder real component
            if cZr*cZr+cZi*cZi > 4: #checks for validity 
                send = False
                iter = N
                break
        if send: #adds to plot if the magnitude of the points is less than 2
            gdots(graph = setg, color = color.red, radius = .3).plot(r, i) #plots points; each dot has a radius of .3 
        else:
          gdots(graph = setg, color = vec(iter/512, iter/32, iter/8), radius = .3).plot(r,i)

def createMag(evt):
    console.log(evt)
    global startMag
    startMag = evt.value
    global smag
    smag.text = '{:1.0f}'.format(startMag*100)+"%"+"\n"

    global setg
    setg.delete()
    setg = graph(title = "Mandelbrot Set", xtitle = "Real", ytitle = "Imaginary", xmax =startX+(2.0)/startMag, xmin = startX+(-2.0)/startMag, ymax = startY+(2.0)/startMag, ymin = startY+(-2.0)/startMag, height  = 650, width = 650)
    for r in range(startX+(-2.0)/startMag,startX+(2.0)/startMag, .02/startMag):   #iterates along the real values; -2, .5 range due to reference: sci-pi.org.uk/mandel/mandel_vs_log.html 
      for i in range(startY+(-2.0)/startMag, startY+(2.0)/startMag, .02/startMag): #iterates along the imaginary values
    
        #TAKES ~2 SECONDS FOR -2,.5,.01; -2,2,.01; N=500 steps
        cZr = r #current Z real component starts at real value r
        cZi = i #current Z imaginary component starts at imaginary value i
        cZr_new = r #creates a placeholder real component used while iterating currentZ values
        send = True
        iter = 0
        for N in range(1000): #iterates current Z imaginary and real components according to Znew = Zcurr**2+Zorig
            cZr_new = cZr*cZr-cZi*cZi+r #placeholder holds iterated real Z component from equation Znew = Zcurr**2+Zorig
            cZi = cZr*cZi*2+i #imaginary Z component from equation Znew = Zcurr**2+Zorig
            cZr = cZr_new #Sets current real Z component equal to the placeholder real component
            if cZr*cZr+cZi*cZi > 4: #checks for validity 
                send = False
                iter = N
                break
        if send: #adds to plot if the magnitude of the points is less than 2
            gdots(graph = setg, color = color.red, radius = .3).plot(r, i) #plots points; each dot has a radius of .3 
        else:
          gdots(graph = setg, color = vec(iter/512, iter/32, iter/8), radius = .3).plot(r,i)

#default code
for r in range(startX+(-2.0)/startMag,startX+(2.0)/startMag, .02/startMag):   #iterates along the real values; -2, .5 range due to reference: sci-pi.org.uk/mandel/mandel_vs_log.html 
    for i in range(startY+(-2.0)/startMag, startY+(2.0)/startMag, .02/startMag): #iterates along the imaginary values
    
        #rate(100000*startMag) #<- procedurally loads the graph by sections
        #TAKES ~2 SECONDS FOR -2,.5,.01; -2,2,.01; N=500 steps
        cZr = r #current Z real component starts at real value r
        cZi = i #current Z imaginary component starts at imaginary value i
        cZr_new = r #creates a placeholder real component used while iterating currentZ values
        send = True
        iter = 0
        for N in range(1000): #iterates current Z imaginary and real components according to Znew = Zcurr**2+Zorig
            cZr_new = cZr*cZr-cZi*cZi+r #placeholder holds iterated real Z component from equation Znew = Zcurr**2+Zorig
            cZi = cZr*cZi*2+i #imaginary Z component from equation Znew = Zcurr**2+Zorig
            cZr = cZr_new #Sets current real Z component equal to the placeholder real component
            if cZr*cZr+cZi*cZi > 4: #checks for validity 
                send = False
                iter = N
                break
        if send: #adds to plot if the magnitude of the points is less than 2
            gdots(graph = setg, color = color.red, radius = .3).plot(r, i) #plots points; each dot has a radius of .3 
        else:
          gdots(graph = setg, color = vec(iter/512, iter/32, iter/8), radius = .3).plot(r,i)

Xslider.disabled = False
Yslider.disabled = False
Magslider.disabled = False
def swap(typeSlider):
    newSlider = typeSlider
    typeSlider.delete()
    typeSlider = newSlider
#Graph takes 1 min ~50 seconds for -2, .5, .001; -2, 2, .001; N=1000 steps

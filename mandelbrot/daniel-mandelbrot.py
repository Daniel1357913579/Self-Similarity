Web VPython 3.2
#creates the graph
set = graph(title = "Mandelbrot Set", xtitle = "Real", ytitle = "Imaginary") 
for r in range(-2,.5,.01):   #iterates along the real values; -2, .5 range due to reference: sci-pi.org.uk/mandel/mandel_vs_log.html 
    for i in range(-2, 2, .01): #iterates along the imaginary values
        #TAKES ~2 SECONDS FOR -2,.5,.01; -2,2,.01; N=500 steps
        cZr = r #current Z real component starts at real value r
        cZi = i #current Z imaginary component starts at imaginary value i
        cZr_new = r #creates a placeholder real component used while iterating currentZ values
        for N in range(100000): #iterates current Z imaginary and real components according to Znew = Zcurr**2+Zorig
            cZr_new = cZr*cZr-cZi*cZi+r #placeholder holds iterated real Z component from equation Znew = Zcurr**2+Zorig
            cZi = cZr*cZi*2+i #imaginary Z component from equation Znew = Zcurr**2+Zorig
            cZr = cZr_new #Sets current real Z component equal to the placeholder real component
        if sqrt(cZr*cZr+cZi*cZi) < 2: #checks for validity 
            gdots(graph = set, color = color.red, radius = .3).plot(r, i) #plots points; each dot has a radius of .3 pixels
#Graph takes 2 min ~18 seconds for -2, .5, .001; -2, 2, .001; N=1000 steps

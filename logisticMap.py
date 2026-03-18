Web VPython 3.2
N = 50
popgraph = graph(title = "Population vs time", xtitle = "Time", ytitle = "Population")
Xpopcurve = gcurve(color = color.blue, graph = popgraph)
Xpopdots = gdots(color = color.purple, graph = popgraph, radius = .3)
Repetitiongraph = graph(title = "Orbit vs Number of Repetitions", xtitle = "Orbit", ytitle = "Number of Repetitions")
Repcountbar = gdots(color = color.red, graph = Repetitiongraph)#doesn't work properly
curr = .4
listX = []
listrep = []
def newPopFrac(r):
    return r*curr*(1-curr)
for i in range(0,4, .001):
    for N in range(1000):
        curr = newPopFrac(i)
        #print("/tN:", N, "I:", i, "current:", curr)
    for N in range(100):
        if any(x <= (curr+.00001) or x >= (curr-.00001) for x in listX):
            if listrep.count(curr) < 1:
                #print("i:",i, "curr:", curr, "count:", listrep.count(curr))
                listrep.append(curr)
            #else:
            #    break
        listX.append(curr)
        curr = newPopFrac(i)
        #print(i, N, curr)
#    print(listrep)
    for iter in range(len(listrep)):
        #print(iter)
        #Xpopcurve.plot(i, listrep[iter])
        Xpopdots.plot(i, listrep[iter])
        #Repcountbar.plot(i, iter)
    listrep = []
    listX = []
    curr = .4
#TEST FILES
#i = 2 
#for N in range(100):
#        curr = newPopFrac(i)
#        print("/tN:", N, "I:", i, "current:", curr)
#for N in range(10):
#    if any(x <= (curr+.001) or x >= (curr-.001) for x in listX):
#        if listrep.count(curr) < 2:
#            print("i:",i, "curr:", curr)
#            listrep.append(curr)
#        else:
#            #break
#            print(listrep)
#    listX.append(curr)
#    curr = newPopFrac(i)
#    print("i:",i, N, curr)
##    print(listrep)
#for iter in range(len(listrep)):
#    #print(iter)
#    Xpopcurve.plot(i, listrep[iter])
#    Xpopdots.plot(i, listrep[iter])
#listrep = []
#listX = []
#curr = .2

Web VPython 3.2
popgraph = graph(title = "Orbit", xtitle = "Time", ytitle = "Population")
Xpopdots = gdots(color = color.purple, graph = popgraph, radius = .3)
curr = .4
listX = []
listrep = []
def newPopFrac(r):
    return r*curr*(1-curr)
  
for i in range(0, 4.1, .001): #runs for all r-values
    for N in range(500): #convergence towards fixed points
            curr = newPopFrac(i) #iterates
      
    for N in range(50): #gets all the repeated values
        if (x <= (curr+.001) or x >= (curr-.001) for x in listX): #compares values to similar previous values
            if listrep.count(curr) < 1:
                listrep.append(curr) #Stores repeated values
                Xpopdots.plot(i, curr) #Plots repeated values
        listX.append(curr) #stores the current value for reference in line 13
        curr = newPopFrac(i) #iterates
      
    listrep = [] #resets list of repeated
    listX = [] #resets list of values
    curr = .4 #resets seed

##TEST FILES
#i = 5
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

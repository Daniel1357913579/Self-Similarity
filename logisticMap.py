Web VPython 3.2
N = 50
popgraph = graph(title = "Population vs time", xtitle = "Time", ytitle = "Population")
Xpopdots = gdots(color = color.purple, graph = popgraph, radius = .3)

#Set the inital values
curr = .4 #The seed value
listX = [] #Inventory of the points that happened in the fixed loop
listrep = []


def newPopFrac(r):
    return r*curr*(1-curr)

#Iterates between 
for i in range(0,4, .001):
    #Iterates through current a certain amount of times
    for N in range(100):
        curr = newPopFrac(i)
    
    for N in range(100):
        if any((x - curr) ** 2 <= 0.00001 for x in listX):
            if listrep.count(curr) < 1:
                listrep.append(curr)
        listX.append(curr)
        curr = newPopFrac(i)
    
    #Plot all the values
    for iter in range(len(listrep)):
        Xpopdots.plot(i, listrep[iter])
        
    #Clear all the values for the next R-value
    listrep = []
    listX = []
    curr = .4

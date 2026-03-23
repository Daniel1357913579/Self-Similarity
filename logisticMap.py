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
for i in range(1,4, .001):
    #Iterates through current a certain amount of times
    for N in range(100):
        curr = newPopFrac(i)
    
    for N in range(100):
        # If the distance between te current position and any x value are te same
        # tis point is going to be considered a repitition point.
        if any(x-curr <= 0.001 or curr-x <= 0.001  for x in listX):
            if listrep.count(curr) < 1:
                #plot the valeus and append it to the list to prevent repetitions
                Xpopdots.plot(i, curr)
                listrep.append(curr)
        listX.append(curr)
        curr = newPopFrac(i)
    

    #Clear all the values for the next R-value
    listrep = []
    listX = []
    curr = .4

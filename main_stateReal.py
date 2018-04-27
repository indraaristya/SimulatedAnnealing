import random
import math


def evaluateX(x,y):

    resultt = (((4 - (2.1*(x**2)) + ((x**4)/3)) * (x**2)) + (x*y) + ((-4 + (4*(y**2)))* (y**2)))

    print ("Current X1: %f" %x)
    print("Current X2: %f" %y)
    print ("f(x1,x2): %f" %resultt)

    return resultt

def evaluateNewXY(x,y):

    result = (((4 - (2.1*(x**2)) + ((x**4) / 3)) * (x ** 2)) + (x * y) + ((-4 + (4 * (y ** 2))) * (y ** 2)))

    print ("New X1: %f" %x)
    print ("New X2: %f" %y)
    print ("f(x1,x2): %f" %result)

    return result

def generateNewXY(currentCoor):
    newstate = currentCoor - random.uniform(-2,2)

    while (-10>newstate or newstate>10):

        newstate = newstate + random.uniform(-2, 2)

    return newstate

def probability(delE,iter):
    return math.exp((-1*delE)/iter)


Cx = random.uniform(-10,10)
Cy = random.uniform(-10,10)

T = 500

bestX = Cx
bestY = Cy

i = 1;

while (T!=0):
    print ("LOOP KE-%d" %i)

    E1 = evaluateX(Cx, Cy) #evaluate current state to get the value of f(x,y)

    newStateX = generateNewXY(Cx) #generate new state
    newStateY = generateNewXY(Cy) #generate new state

    E2 = evaluateNewXY(newStateX,newStateY) #evaluate new state to get the value of f(x,y)

    if (E2 < E1): #compare; if new state better than current state (f(x,y)new < f(x,y)current
        Cx = newStateX
        Cy = newStateY
        bestX = newStateX
        bestY = newStateY
    else:
        deltaE = (E2 - E1)
        p = probability(deltaE,T)
        r = random.uniform(0,1)
        if (r < p):
            Cx = newStateX
            Cy = newStateY
    i = i+1
    T = T - 0.5
    print("")

print("")
print("")
bestF = evaluateX(bestX,bestY)
print("BEST SEARCH")
print(bestF)
*****targil 8:

def getCircleHekef(radius):
    hekef = (radius * math.pi)*2
    return hekef
    
*****targil 9:

def add(x = 0, y = 0):
    return  x + y

def sub(x = 0, y = 0):
    return x - y

def mul(x = 0, y = 0):
    return x * y

def div(x = 0, y = 0):
    return x / y
    
*****targil 10:

def getInRange(min = 10, max = 100):
    while True:
        num = int(input("please enter number: "))
        if num >= min and num <= max:
            return num
            
*****targil 11:

def getMin(x,y,z):
    min = x
    if y < min:
        min = y
    if z < min:
        min = z
    return min

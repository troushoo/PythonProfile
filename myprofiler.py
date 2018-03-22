def myfunc2(count):
        x = 1
        y = 2
        z = 1

        while (count>0):
                z = x + y
                x = y * z
                y = y + x
                count-=1

def myfunc1(x):
        myfunc2(x)

def myfuncc(x):
        myfunc2(x)

def myfuncb(x):
        myfuncc(x)

def myfunca(x):
        myfuncb(x)

while (True):
        myfunc1(5)
        myfunca(10)

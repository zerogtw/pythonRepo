from functools import reduce

def normalize(name):
    return name[:1].upper() + name[1:].lower()

def prod(L):
    def f(x, y):
        l = []
        while y > 0:
            l.append(x)
            y = y-1 
        return sum(l)
    return reduce(f,list(L))

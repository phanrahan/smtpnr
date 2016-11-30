from pnr import *


def And4():
    return Node(Node(), Node(), Node(), Node())

def Mux2():
    x = Node()
    y = Node()
    return Node(x,y)

def Mux4():
    return Node(Mux2(), Mux2())

def Mux8():
    return Node(Mux4(), Mux4())

def DAG():
    x = Node()
    y = Node()
    z = Node(x,y)
    return Node(x,z)


def doit(nodes):
    s = setup(nodes)

    # s.add(root.x == 0, root.y == 0)

    minarea = 100
    minm = None
    minxl = 0
    minyl = 0
    for m in getmodels(s, 100):
        #printmodel(m, nodes)
        xmin, xmax, ymin, ymax = bbox(m, nodes)
        xl = xmax-xmin+1
        yl = ymax-ymin+1
        area = xl*yl
        if area < minarea:
           minxl = xl
           minyl = yl
           minarea = area
           minm = m

    printmodel(minm, nodes)
    print 'bbox', minxl, minyl

if __name__ == "__main__":
    doit(Mux8().flatten())

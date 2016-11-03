import sys
from z3 import *

def fullnode(n, m):
    return "%s@(%s,%s)" % (str(n), str(m.evaluate(n.x)), str(m.evaluate(n.y)))

def printmodel(m, nodes):
    for n in nodes:
        if n.inputs:
            print "%s" % fullnode(n, m),
            print 'is connected to',
            for i in n.inputs:
                print '%s' % fullnode(i,m),
            print

    xmin, xmax, ymin, ymax = bbox(m, nodes)
    for y in range(ymax,ymin-1,-1):
        for x in range(xmin,xmax+1):
            s = '   '
            for n in nodes:
                xn = int(str(m.evaluate(n.x)))
                yn = int(str(m.evaluate(n.y)))
                if x == xn and y == yn:
                    s = "%3s" % str(n)
            print s,
        print


def getmodels(s, n):
    for i in range(n):
        if s.check() != sat:
            break
        m = s.model()
        # Create a new constraint the blocks the current model
        block = []
        for d in m:
            # d is a declaration
            if d.arity() > 0:
                raise Z3Exception("uninterpreted functions are not supported")
            # create a constant from declaration
            c = d()
            if is_array(c) or c.sort().kind() == Z3_UNINTERPRETED_SORT:
                raise Z3Exception("arrays and uninterpreted sorts are not supported")
            block.append(c != m[d])
        yield m
        #print 'adding', block
        s.add(Or(block))
    raise StopIteration

class Node:
    nextn = 0
    def __init__(self, *inputs, **kwargs):
        self.name = kwargs.get('name', None)
        self.inputs = inputs

        self.n = Node.nextn
        Node.nextn += 1

        self.x = Int("x"+str(self.n))
        self.y = Int("y"+str(self.n))

        self.mark = False

    def __repr__(self):
        return str(self.n)

    def __str__(self):
        return str(self.n)

    def flatten(self):
         n = []
         if not self.mark:
             for i in self.inputs:
                 n += i.flatten()
             n += [self]
             self.mark = True
         return n

    def connections(self, solver, htrack=False, vtrack=False, neighbors=True):
        for i in self.inputs:
            if neighbors:
                # connect to 1 of your 8 nearest neightbors
                if not htrack and not vtrack:
                    solver.add(Or( And(self.x-i.x==  0, self.y-i.y== -1), 
                                   And(self.x-i.x==  0, self.y-i.y==  1), 
                                   And(self.x-i.x== -1, self.y-i.y==  0),
                                   And(self.x-i.x==  1, self.y-i.y==  0),
                                   And(self.x-i.x== -1, self.y-i.y== -1),
                                   And(self.x-i.x== -1, self.y-i.y==  1), 
                                   And(self.x-i.x==  1, self.y-i.y== -1),
                                   And(self.x-i.x==  1, self.y-i.y==  1)))
                else:
                    if vtrack:
                        solver.add(Or(self.x == i.x,
                                      And(self.x-i.x== -1, self.y-i.y==  0), 
                                      And(self.x-i.x==  1, self.y-i.y==  0),
                                      And(self.x-i.x== -1, self.y-i.y== -1),
                                      And(self.x-i.x== -1, self.y-i.y==  1), 
                                      And(self.x-i.x==  1, self.y-i.y== -1),
                                      And(self.x-i.x==  1, self.y-i.y==  1)))
            else:
                if   htrack and vtrack:
                    # connect vertically or horizontally
                    solver.add(Or(self.x == i.x, self.y == i.y))
                elif vtrack:
                    solver.add(self.x == i.x)
                elif htrack:
                    solver.add(self.y == i.y)

def overlaps(solver, nodes):
    n = len(nodes)
    for i in range(n):
        for j in range(i+1, n):
             solver.add(Or(nodes[i].x != nodes[j].x, nodes[i].y != nodes[j].y))
                 

def setup(nodes, htrack=False, vtrack=False, neighbors=True):
    s = Solver()

    for n in nodes:
        n.connections(s, htrack, vtrack, neighbors)
    overlaps(s, nodes)

    return s

def bbox(m, nodes):
    xmin =  sys.maxint
    xmax = -sys.maxint-1
    ymin =  sys.maxint
    ymax = -sys.maxint-1
    for n in nodes:
        x = int(str(m.evaluate(n.x)))
        if x < xmin: xmin = x
        if x > xmax: xmax = x
        y = int(str(m.evaluate(n.y)))
        if y < ymin: ymin = y
        if y > ymax: ymax = y
    #print 'x', xmin, xmax, 'y', ymin, ymax
    return xmin, xmax, ymin, ymax

def stats(m, nodes):
    xmin =  sys.maxint
    xmax = -sys.maxint-1
    ymin =  sys.maxint
    ymax = -sys.maxint-1
    for n in nodes:
        x = int(str(m.evaluate(n.x)))
        y = int(str(m.evaluate(n.y)))
        if x < xmin: xmin = x
        if y < ymin: ymin = y
        if x > xmax: xmax = x
        if y > ymax: ymax = y

    connections = 0
    tracks = 0
    length = 0
    for n in nodes:
        x = int(str(m.evaluate(n.x)))
        y = int(str(m.evaluate(n.y)))
        for i in n.inputs:
            xi = int(str(m.evaluate(i.x)))
            yi = int(str(m.evaluate(i.y)))
            connections += 1
            if (abs(xi-x) > 1) or (abs(yi-y) > 1): 
                tracks += 1
                assert (xi == x) or (yi == y)
                if xi == x:
                    length += abs(yi-y)
                if yi == y:
                    length += abs(xi-x)

    print connections-tracks, 'nearest neighbor connections'
    print tracks, 'vertical tracks', 
    print 'length=%d (%g)' % (length, float(length)/tracks)
    print 'bbox', xmax-xmin+1, ymax-ymin+1

    return tracks, length


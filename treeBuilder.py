import exprUtils

class Node:

    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def display(self):
        print("(",end='')
        self.left.display()
        print(self.op,end='')
        self.right.display()
        print(")",end='')

    def eval(self):
        leftVal = self.left.eval()
        rightVal = self.right.eval()

        if(leftVal == None or rightVal == None):
            return None

        if(self.op == "+"):
            return leftVal + rightVal
        elif(self.op == "-"):
            return leftVal - rightVal
        elif(self.op == "*"):
            return leftVal * rightVal
        elif(self.op == "/"):
            if(rightVal == 0):
                return None
            return leftVal / rightVal



class Leaf:

    def __init__ (self, data):
        self.data = data

    def display(self):
        print(self.data,end='')

    def eval(self):
        return self.data


def formatToMinDp(num):
    if(num % 1 == 0):
        return str(int(num))
    else:
        return str(num)


def parse(expr):

    if(exprUtils.isVal(expr)):
        return Leaf(float(expr))

    left,op,right = exprUtils.splitIntoParts(expr)

    if (op == None) :
        return None


    ltree = parse(left)
    rtree = parse(right)

    if(ltree == None or rtree == None) :
        return None
    
    return Node(ltree, op, rtree)


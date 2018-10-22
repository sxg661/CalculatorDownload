import re

def isVal(expr):

    matches = re.search("-?[0-9]+(\.[0-9]+)?", expr)

    if(not matches):
        return False
    
    return (matches[0] == expr)
        

def trimBrackets(expr):
    #gets rid of surrounding brackets if there are any

    if(len(expr) == 0):
        return expr
    
    if(expr[0] == '(') and (expr[len(expr) - 1] == ')'):
        closingIndex = -1;
        i = 1
        brdepth = 0
        while(i < len(expr)):
            if(expr[i] == '('):
                brdepth +=1
            elif(expr[i] == ')'):
                if(brdepth == 0):
                    closingIndex = i
                    break
                brdepth -= 1
            i += 1

        if(closingIndex == len(expr) - 1):
            return expr[1 : len(expr) - 1]

    return expr



    



def splitIntoParts(expr):

    expr = trimBrackets(expr)

    splitIndex = findHighestOp(expr)

    if splitIndex == None:
        return None, None, None

    leftSide = expr[0:splitIndex]
    operator = expr[splitIndex]
    rightSide = expr[splitIndex + 1:]

    return leftSide, operator, rightSide
    

def getPrecedence(op):
    return ['+','-','*','/'].index(op)

def findHighestOp(expr):
    brackDepth = 0
    opIndex = None
    maxPre = 100
    for i in range(0, len(expr)):
        if expr[i] == '(':
            brackDepth += 1
        elif expr[i] == ')':
            brackDepth -= 1
        elif expr[i] in '+-*/':

            #shows the operator is not in the right place
            #(in case of minus signs)
            if(i == 0 or expr[i - 1] in '+-*/'):
                continue

            #if we're not at minimum bracket depth then ignore
            if(brackDepth != 0):
                continue

            pre = getPrecedence(expr[i])

            if(pre < maxPre):
                maxPre = pre
                opIndex = i
                
    return opIndex



            

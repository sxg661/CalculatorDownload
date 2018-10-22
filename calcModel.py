import treeBuilder

class CalcModel:
    def __init__(self):
        self.text = ""
        self.frozen = False

    def isFrozen(self):
        return self.frozen


    def currentText(self):
        return self.text

    def addToText(self, append):
        if(len(self.text) < 40):
            self.text = self.text + append
        return self.text

    def backspace(self):
        if(len(self.text) > 0):
            self.text = self.text[0 : len(self.text) - 1]
        return self.text

    def clear(self):
        self.text = ""
        self.frozen = False
        return self.text

    def evaluate(self):
        parseTree = treeBuilder.parse(self.text)
        
        if(parseTree == None):
            self.text = "Syntax Error"
        else:
            self.text = parseTree.eval()
            if (self.text == None):
                self.text = "Maths Error"
            else:
                self.text = treeBuilder.formatToMinDp(self.text)

        self.frozen = True

        return self.text
        
        

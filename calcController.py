import calcModel

class CalcController():

    def __init__(self):
        self.model = calcModel.CalcModel()

    def handleInput(self, text):

        if(text == "AC"):
            return self.model.clear()

        if(not self.model.isFrozen()):
            if(text == "DEL"):
                return self.model.backspace()
            elif(text == "="):
                return self.model.evaluate()
            else:
                return self.model.addToText(text)

        return self.model.currentText()
        

    

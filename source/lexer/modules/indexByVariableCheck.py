# --- Clean var index constructor, used in lexer ---       
def indexByVariableCheck(self):
    numbers = self.tokenize(self.lexerOutputPart)

    if self.indexByVariable not in self.variables:
        self.variables[self.indexByVariable]= "00"

    self.indexByVariable = int(self.variables[self.indexByVariable])

    if 0 <= self.indexByVariable < len(numbers):
        self.lexerOutputPart = numbers[self.indexByVariable]

    else:
        if numbers:
            self.lexerOutputPart = numbers[-1]
            
        else:
            self.lexerOutputPart = "00"

    self.indexByVariable = ""
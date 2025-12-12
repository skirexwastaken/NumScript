# --- Cleans var constructor, used in lexer ---
def variableByVariableCheck(self):
    if self.variableByVariable not in self.variables:
        self.variables[self.variableByVariable] = "00"

    variableName = self.variables[self.variableByVariable]

    if variableName not in self.variables:
        self.variables[variableName] = "00"

    self.lexerOutputPart += self.variables[variableName]
    self.variableByVariable = ""
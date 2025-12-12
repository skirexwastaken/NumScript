# --- Cleans var constructor, used in lexer ---
def variableByNumberCheck(self):
    if self.variableByNumber not in self.variables:
        self.variables[self.variableByNumber] = "00"

    self.lexerOutputPart += self.variables[self.variableByNumber]

    self.variableByNumber = ""
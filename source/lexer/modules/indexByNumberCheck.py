# --- Clean num index constructor, used in lexer ---
def indexByNumberCheck(self):
    self.indexByNumber=int(self.indexByNumber)
    numbers = self.tokenize(self.lexerOutputPart)

    if 0 <= self.indexByNumber < len(numbers):
        self.lexerOutputPart = numbers[self.indexByNumber]

    else:
        if numbers:
            self.lexerOutputPart = numbers[-1]
        
        else:
            self.lexerOutputPart = "00"

    self.indexByNumber = ""
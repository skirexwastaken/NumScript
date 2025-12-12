# --- Tokenizes code from input ---
def tokenizer(self,line):
    if line.isdigit(): #Checks if there are only numbers in line
        if len(line) % 2 != 0:
            line+="0" #Checks if line is in correct pair number format

        return(self.tokenize(line))

    elif line == "":
        return(self.tokenize("00"))

    else:
        numericalLine=""

        for symbol in line:
            if symbol.isdigit():
                numericalLine += symbol
                
            elif symbol in self.reversedNSAscii:
                numericalLine += self.reversedNSAscii[symbol]
                
            else:
                numericalLine += "00"

        return(self.tokenize(numericalLine))
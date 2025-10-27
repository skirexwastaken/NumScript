# --- Tokenizes code from input ---
def tokenizer(self,line):
    if line.isdigit():#Checks if there are only numbers in line
        if len(line) % 2 != 0:
            line+="0"#Checks if line is in correct pair number format
        
        return(self.tokenize(line))

    else:
        numerical_line=""
        for i in line:
            if i.isdigit():
                numerical_line+=i
                
            elif i in self.reversed_nsascii:
                numerical_line+=self.reversed_nsascii[i]
                
            else:
                numerical_line+="00"
        return(self.tokenize(numerical_line))
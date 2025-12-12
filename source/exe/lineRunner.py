# --- Function that runs tokenized code in a list, used in exe ---        
def lineRunner(self, currentTokenizedCode, index):
    line = self.parser(currentTokenizedCode[index])

    # --- No error ---
    if line[0] != "-":
        if self.states["splitter"]:
            print(self.shellOutSymbol + ' '.join([line[i:i + 2] for i in range(0, len(line), 2)]))

        else:
            print(f"{self.shellOutSymbol}{line}")
            
    # --- Error code --
    else:
        if self.states["debug"]:
            print(f"{self.shellOutSymbol}{line.replace("-", "")}")

    # --- Printing tokens ---
    if self.states["printTokens"]:
        print(f"{self.shellOutSymbol}{currentTokenizedCode[index]}")

    # --- Printing memory ---
    if self.states["printMemory"]:
        print(f"{self.shellOutSymbol}{self.variables}\n{self.definitions}\n{self.stacks}")
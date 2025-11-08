# --- Function that runs tokenized code in a list, used in exe ---        
def line_runner(self,current_tokenized_code,index):
    line = self.parser(current_tokenized_code[index])

    # --- No error ---
    if line[0] != "-":
        if self.states["splitter"]:
            print(self.shell_out_symbol+' '.join([line[i:i+2] for i in range(0, len(line), 2)]))

        else:
            print(f"{self.shell_out_symbol}{line}")
            
    # --- Error code --
    else:
        if self.states["debug"]:
            print(f"{self.shell_out_symbol}{line.replace("-","")}")

    # --- Printing tokens ---
    if self.states["print_tokens"]:
        print(f"{self.shell_out_symbol}{current_tokenized_code[index]}")

    # --- Printing memory ---
    if self.states["print_memory"]:
        print(f"{self.shell_out_symbol}{self.variables}\n{self.definitions}\n{self.pointers}")
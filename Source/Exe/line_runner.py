# --- Function that runs tokenized code in a list, used in exe ---        
def line_runner(self,current_tokenized_code,index):
    line = current_tokenized_code[index]#Grabs a line of code

    if isinstance(line, list):#Checks if current line is valid
        line = self.parser(line)#Runs the line thru parser

        if line:

            if line != "" and not line[0]=="-":#Checks if there's no error
                if self.states["splitter"]:
                    print(self.shell_out_symbol+' '.join([line[i:i+2] for i in range(0, len(line), 2)]))#If splitter is turned on, the tokens will be split by " "

                else:
                    print(f"{self.shell_out_symbol}{line}")#If splitter is turned off, the tokens will be simply printed

            else:#If there's an error or internal process
                if self.states["debug"]:
                    print(f"{self.shell_out_symbol}{line.replace("-","")}")#If debug is on, the message will be printed

            if self.states["print_tokens"]:
                print(f"{self.shell_out_symbol}{current_tokenized_code[index]}")#If print tokens state is set to true, prints the original line of code

            if self.states["print_memory"]:
                print(f"{self.shell_out_symbol}{self.variables}\n{self.definitions}\n{self.pointers}")#If print variables state is set to true, variable and definiton variables will be printed  

    else:#If there's an error in tokenizer
        if self.states["debug"]:
            print(f"{self.shell_out_symbol}{line}")#If debug is on, the error message will be printed
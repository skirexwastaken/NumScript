# --- Importing Libraries ---
import sys
import os

# --- NumScript cli that can run from file or from CLI input ---        
def cli(self):

    # --- Asci Console Art ---
    self.ascii_art()

    # --- Running code from .ns file ---
    if len(sys.argv) > 1: #File input from system arguments
        NSfile = sys.argv[1].replace("\\","/")#Replaces \\ with / for "open" to work

        if os.path.exists(NSfile) and NSfile.endswith(".ns"):
            with open(NSfile, 'r', encoding='utf-8') as NSCode:

                for line in NSCode:
                    line = line.replace(" ", "").rstrip()

                    if line and line != "\n": # check for empty lines
                        tokenized_line = self.tokenizer(line)

                        if tokenized_line != "-99":
                            self.tokenized_code.append(tokenized_line)
            self.run()
            exit()

        else:
            exit()

    # --- Console Interface ---        
    while True:
        line = input(self.shell_in_symbol).replace(" ","")

        if line != "":
            tokenized_line = self.tokenizer(line)

            if tokenized_line == ["00"]:
                self.run()

            elif len(tokenized_line) > 2:
                if tokenized_line[-2] == "25" and tokenized_line[-1] == "00":
                    self.tokenized_code.append(tokenized_line[:-2])
                    self.run()

                elif tokenized_line != "-99":
                    self.tokenized_code.append(tokenized_line)
                    
            elif tokenized_line != "-99":
                    self.tokenized_code.append(tokenized_line)
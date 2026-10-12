# GNU GENERAL PUBLIC LICENSE
# Version 3, 29 June 2007
#
# Copyright (C) 2026 Daniel Hora
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

# --- Importing Libraries ---
import sys
import os

# --- NumScript cli that can run from file or from cli input ---
def cli(self):

    # --- Asci Console Art ---
    self.asciiArt()

    # --- Running code from .ns file ---
    if len(sys.argv) > 1: #File input from system arguments
        NSfile = sys.argv[1].replace("\\","/") #Replaces \\ with / for "open" to work

        if os.path.exists(NSfile) and NSfile.endswith(".ns"):
            with open(NSfile, 'r', encoding='utf-8') as NSCode:

                for line in NSCode:
                    line = line.replace(" ", "").rstrip()

                    if line and line != "\n": #Check for empty lines
                        tokenizedLine = self.tokenizer(line)

                        self.tokenizedCode.append(tokenizedLine)
            self.run()
            exit()

        else:
            exit()

    # --- Console Interface ---        
    while True:
        line = input(self.shellInSymbol)

        if line != "":
            tokenizedLine = self.tokenizer(line)

            if tokenizedLine == ["00"]:
                self.run()

            elif len(tokenizedLine) > 2:
                if tokenizedLine[-2] == "25" and tokenizedLine[-1] == "00":
                    self.tokenizedCode.append(tokenizedLine[:-2])
                    self.run()

                elif tokenizedLine != "-99":
                    self.tokenizedCode.append(tokenizedLine)
                    
            elif tokenizedLine != "-99":
                    self.tokenizedCode.append(tokenizedLine)
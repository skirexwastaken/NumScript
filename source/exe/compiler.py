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

# --- Compiles NS code to more simple variant ---
def compiler(self, parsedTokenizedCode):

    # --- Declaring needed variables ---
    tokenizedCodeIndex = 0
    tokenizedLineIndex = 0
    skip = False

    # --- Going thru every line of code in tokenized code ---
    while tokenizedCodeIndex < len(parsedTokenizedCode):
        tokenizedLine = parsedTokenizedCode[tokenizedCodeIndex]
        tokenizedLineIndex = 0
    
        while tokenizedLineIndex < len(tokenizedLine):
            token = tokenizedLine[tokenizedLineIndex]
            
            if not skip:
                match token:
            
                    case "01"|"02"|"03"|"04"|"05"|"08"|"09":
                        skip=True
                
                    case "06"|"07":
                        return(parsedTokenizedCode)
                
                    case "25":
                        parsedTokenizedCode[tokenizedCodeIndex] = tokenizedLine[:tokenizedLineIndex]
                        parsedTokenizedCode.insert(tokenizedCodeIndex + 1, tokenizedLine[tokenizedLineIndex + 1:])
                        tokenizedLine = tokenizedLine[:tokenizedLineIndex]
                                    
            else: skip = False
        
            tokenizedLineIndex += 1
        tokenizedCodeIndex += 1
            
    return(parsedTokenizedCode)
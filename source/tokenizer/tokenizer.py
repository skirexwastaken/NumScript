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

# --- Tokenizes code from input ---
def tokenizer(self,line):
    if isinstance(line,str):
        line = line.replace(" ","")

        numericalLine = ""
        for symbol in line:
            if symbol.isdigit():
                numericalLine += symbol

            elif symbol in self.reversedNSAscii:
                numericalLine += self.reversedNSAscii[symbol]

            else:
                numericalLine += "00"

        if len(numericalLine) % 2 != 0:
            numericalLine = self.rounder(numericalLine)

        return(self.tokenize(numericalLine))

    else:
        return(self.tokenize("00"))
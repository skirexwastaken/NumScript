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

# --- Function that runs tokenized code in a list, used in exe ---        
def lineRunner(self, currentTokenizedCode, index):
    line = self.interpreter(currentTokenizedCode[index])

    # --- No error ---
    if line[0] != "-":
        if self.states["splitter"]:
            self.handleOutput(self.shellOutSymbol + ' '.join([line[i:i + 2] for i in range(0, len(line), 2)]))

        else:
            self.handleOutput(f"{self.shellOutSymbol}{line}")
            
    # --- Error code --
    else:
        if self.states["debug"]:
            self.handleOutput(f"{self.shellOutSymbol}{line.replace("-", "")}")

    # --- Printing tokens ---
    if self.states["printTokens"]:
        self.handleOutput(f"{self.shellOutSymbol}{currentTokenizedCode[index]}")

    # --- Printing memory ---
    if self.states["printMemory"]:
        self.handleOutput(f"{self.shellOutSymbol}{self.variables}\n{self.definitions}\n{self.stacks}")
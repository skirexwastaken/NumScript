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

# --- Clean var index constructor, used in operandAssembler ---       
def indexByVariableCheck(self):
    numbers = self.tokenize(self.operandAssemblerOutputPart)

    if self.indexByVariable not in self.variables:
        self.variables[self.indexByVariable]= "00"

    self.indexByVariable = int(self.variables[self.indexByVariable])

    if 0 <= self.indexByVariable < len(numbers):
        self.operandAssemblerOutputPart = numbers[self.indexByVariable]

    else:
        if numbers:
            self.operandAssemblerOutputPart = numbers[-1]
            
        else:
            self.operandAssemblerOutputPart = "00"

    self.indexByVariable = ""
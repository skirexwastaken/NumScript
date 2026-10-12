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

# --- Utility for operandAssembler ---        
def operandAssemblerUtility(self, skip):
    
    # --- skip defines which function is not to be ran ---   
    if skip != "cleanVariableByNumber" and self.variableByNumber:
        self.variableByNumberCheck()
        
    if skip != "cleanVariableByVariable" and self.variableByVariable:
        self.variableByVariableCheck()
        
    if skip != "cleanIndexByVariable" and self.indexByVariable:
        self.indexByVariableCheck()
        
    if skip != "cleanIndexByNumber" and self.indexByNumber:
        self.indexByNumberCheck()

    if skip != "cleanstackByNumber" and self.stackByNumber:
        self.stackByNumberCheck()
        
    if skip != "cleanstackByVariable" and self.stackByVariable:
        self.stackByVariableCheck()
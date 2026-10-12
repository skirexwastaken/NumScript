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

# --- Function that allows NumScript to be embeded inside of .py files ---
def container(self,code):
    """
    Alternative run function that can be embeded inside of regular python files.
    It can take both single line of a code or a list of code.
    Example usage: number = container("10 01 10 30 01 05")
    """

    # --- Overwriting NSVM settings for the container to work properly ---
    self.shellOutput = False
    self.shellOutSymbol = ""

    # --- Loading code into tokenized code ---
    if isinstance(code,str):
        self.tokenizedCode.append(self.tokenizer(code))

    elif isinstance(code,list):
        for line in code:
            self.tokenizedCode.append(self.tokenizer(line))

    # --- NSVM is restarted after the code execution ---
    self.tokenizedCode.append("21")
    
    # --- Executing the code ---
    self.run()

    # --- Returning output ---

    return self.nsOut

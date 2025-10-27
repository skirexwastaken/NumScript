# --- Cleans var constructor, used in lexer ---
def variable_by_number_check(self):

    if self.variable_by_number not in self.variables:
        self.variables[self.variable_by_number]="00"

    self.output_value+=self.variables[self.variable_by_number]

    self.variable_by_number=""
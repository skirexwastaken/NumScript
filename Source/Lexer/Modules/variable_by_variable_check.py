# --- Cleans var constructor, used in lexer ---
def variable_by_variable_check(self):
    if self.variable_by_variable not in self.variables:
        self.variables[self.variable_by_variable]="00"

    self.output_value+=self.variables[self.variables[self.variable_by_variable]]
    self.variable_by_variable=""
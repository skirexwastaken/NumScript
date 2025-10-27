# --- Calls ta pointer where its name is a value of a variable ---        
def pointer_by_variable_check(self):
    if self.variables[self.pointer_by_variable] not in self.pointers:
        return ""

    self.variables = self.pointers[self.variables[self.pointer_by_variable]]

    for variable in self.variables:
        if variable not in self.variables:
            self.variables[variable]="00"

        self.output+=self.variables[variable]

    self.pointer_by_variable=""
# --- Calls a pointer where its name is a number ---        
def pointer_by_number_check(self):
    if self.pointer_by_number not in self.pointers:
        return 

    self.variables = self.pointers[self.pointer_by_number]

    for variable in self.variables:
        if variable not in self.variables:
            self.variables[variable]="00"

        self.output+=self.variables[variable]

    self.pointer_by_number=""
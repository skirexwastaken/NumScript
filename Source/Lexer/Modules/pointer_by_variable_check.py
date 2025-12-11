# --- Calls ta pointer where its name is a value of a variable ---        
def pointer_by_variable_check(self):
    if self.variables[self.pointer_by_variable] not in self.pointers:
        return ""
    
    if len(self.pointers[self.variables[self.pointer_by_variable]]) != 0:

        self.output_value+=self.variables[self.pointers[self.variables[self.pointer_by_variable]][-1]]

        del self.pointers[self.variables[self.pointer_by_variable]][-1]

    self.pointer_by_variable=""
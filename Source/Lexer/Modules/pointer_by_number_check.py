# --- Calls a pointer where its name is a number ---        
def pointer_by_number_check(self):
    if self.pointer_by_number not in self.pointers:
        return ""

    if len(self.pointers[self.pointer_by_number]) != 0:

        self.output_value+=self.variables[self.pointers[self.pointer_by_number][-1]]

        del self.pointers[self.pointer_by_number][-1]

    self.pointer_by_number=""
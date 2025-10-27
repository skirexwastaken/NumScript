# --- Clean var index constructor, used in lexer ---       
def index_by_variable_check(self):
    numbers=self.tokenize(self.output_value)

    if self.index_by_variable not in self.variables:
        self.variables[self.index_by_variable]="00"

    self.index_by_variable=int(self.variables[self.index_by_variable])

    if 0 <= self.index_by_variable < len(numbers):
        self.output_value=numbers[self.index_by_variable]

    else:
        if numbers:
            self.output_value = numbers[-1]
            
        else:
            self.output_value = "00"

    self.index_by_variable=""
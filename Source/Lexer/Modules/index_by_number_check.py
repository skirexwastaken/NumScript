# --- Clean num index constructor, used in lexer ---
def index_by_number_check(self):
    self.index_by_number=int(self.index_by_number)
    numbers=self.tokenize(self.output_value)

    if 0 <= self.index_by_number < len(numbers):
        self.output_value = numbers[self.index_by_number]

    else:
        if numbers:
            self.output_value = numbers[-1]
        
        else:
            self.output_value = "00"

    self.index_by_number=None
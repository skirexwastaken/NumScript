# --- Utility for lexer ---        
def lexer_utility(self, to_clean):
    
    # --- to_clean defines which function is not to be ran ---   
    if to_clean != "clean_variable_by_number" and self.variable_by_number != "":    
        self.variable_by_number_check()
        
    if to_clean != "clean_variable_by_variable" and self.variable_by_variable != "":    
        self.variable_by_variable_check()
        
    if to_clean != "clean_index_by_variable" and self.index_by_variable != "":
        self.index_by_variable_check()
        
    if to_clean != "clean_index_by_number" and self.index_by_number != "":  
        self.index_by_number_check()

    if to_clean != "clean_pointer_by_number" and self.pointer_by_number != "":    
        self.pointer_by_number_check()
        
    if to_clean != "clean_pointer_by_variable" and self.pointer_by_variable != "":   
        self.pointer_by_variable_check()  
# --- Compiles NS code to more simple variant ---
def compiler(self, parsed_tokenized_code):

    # --- Declaring needed variables ---
    tokenized_code_index=0
    tokenized_line_index=0
    skip=False

    # --- Going thru every line of code in tokenized code ---
    while tokenized_code_index < len(parsed_tokenized_code):
        tokenized_line=parsed_tokenized_code[tokenized_code_index]
        tokenized_line_index=0
    
        while tokenized_line_index < len(tokenized_line):  
            token=tokenized_line[tokenized_line_index]
            
            if not skip:
                match token:
            
                    case "01"|"02"|"03"|"04"|"05"|"08"|"09":
                        skip=True
                
                    case "06"|"07":
                        return(parsed_tokenized_code)
                
                    case "25":
                        parsed_tokenized_code[tokenized_code_index]=tokenized_line[:tokenized_line_index]
                        parsed_tokenized_code.insert(tokenized_code_index+1,tokenized_line[tokenized_line_index+1:])
                        tokenized_line=tokenized_line[:tokenized_line_index]
                                    
            else:skip=False
        
            tokenized_line_index+=1  
        tokenized_code_index+=1
            
    return(parsed_tokenized_code)
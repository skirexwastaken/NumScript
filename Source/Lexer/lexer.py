# --- Importing Libraries ---
import random
import re
from datetime import datetime

# --- Analyses code, used in most NS functions ---    
def lexer(self,tokens):

    # --- Declaring variables used in lexer ---
    skip = False
    index = 0
    tokens = tokens[1:]
    
    # --- The idea here is that a buffer is added at the start so in case there's for example 01 at the end of the line the lexer won't crash ---
    tokensLength = len(tokens)
    tokens.append("00")
    
    deleted = 0
    
    self.output_value = ""
    self.output = []

    self.variable_by_number =""
    self.variable_by_variable = ""

    self.index_by_number = ""
    self.index_by_variable = ""

    self.pointer_by_number = ""
    self.pointer_by_variable = ""

    # --- Building print value ---
    for token in range(tokensLength):
        
        # --- Skip is used to distinguish between pair and non pair tokens ---
        if not skip:

            # --- Match used to grab the current token ---    
            match tokens[index]:
            
                # --- Checking for number ---
                case"01":
                    self.lexer_utility(None)

                    self.output_value+=tokens[index+1]
                    skip=True

                # --- Checking for variable ---    
                case"02":
                    self.lexer_utility("clean_variable_by_number")
                    
                    self.variable_by_number+=tokens[index+1]
                    skip=True

                # --- Checking for variable with name being variable value ---
                case"03":
                    self.lexer_utility("clean_variable_by_variable")

                    self.variable_by_variable+=tokens[index+1]
                    skip=True

                    # --- Grabs item by num index from the existing code ---    
                
                case"04":
                    self.lexer_utility("clean_index_by_number")

                    self.index_by_number+=tokens[index+1]
                    skip=True

                # --- Grabs item by var index from the existing code ---    
                case"05":
                    self.lexer_utility("clean_index_by_variable")

                    self.index_by_variable+=tokens[index+1]
                    skip=True

                # --- Rest is num ---    
                case"06":
                    self.lexer_utility(None)

                    tokens=tokens[index+1:]
                    self.output_value+="".join(tokens)
                    index=len(tokens)-1

                # --- Rest is var ---
                case"07":
                    self.lexer_utility(None)

                    tokens=tokens[index+1:]
                    self.variable_by_number+="".join(tokens)
                    index=len(tokens)-1

                # --- Call pointer with num value ---    
                case"08":
                    self.lexer_utility("clean_pointer_by_number")

                    self.pointer_by_number+=tokens[index+1]
                    skip=True

                # --- Call pointer with var value ---
                case"09":
                    self.lexer_utility("cleen_pointer_by_variable")

                    self.pointer_by_variable+=tokens[index+1]
                    skip=True

                # --- Input ---    
                case"12":
                    self.lexer_utility(None)

                    inputed_code = self.tokenizer(input(self.input_symbol).replace(" ",""))

                    if isinstance(inputed_code, list):
                        self.output_value+="".join(inputed_code)

                # --- Comment ---        
                case"22":
                    break

                # --- Checking for split between variable/variable ---            
                case"23":
                    self.clean_var_num()

                # --- Checking for split between parts ---
                case"24":
                    self.lexer_utility(None)

                    self.output.append(self.output_value)
                    self.output_value=""

                # --- Adds day/month/year ---
                case"26":
                    self.lexer_utility(None)

                    now=datetime.now()
                    self.output_value+=self.rounder(str(now.day))+self.rounder(str(now.month))+self.rounder(str(now.year))

                # --- Adds hour/minute ---   
                case"27":
                    self.lexer_utility(None)

                    now=datetime.now()
                    self.output_value+=self.rounder(str(now.hour))+self.rounder(str(now.minute)) 

                # --- Checking for math logic ---
                case"30"|"31"|"32"|"33"|"34"|"35"|"36"|"37"|"38"|"39":    
                    self.lexer_utility(None)

                    self.output_value+={"30":"++","31":"--","32":"**","33":"//","34":">>","35":"<<","36":"==","37":"&&","38":"||","39":"~~"}[tokens[index]]
            
                # --- Min ---
                case"70":
                    self.lexer_utility(None)
                
                    if self.output_value == "":
                        self.output_value="00"

                    numbers = self.tokenize(self.output_value)
                    self.output_value=str(min(numbers))

                # --- Max ---    
                case"71":
                    self.lexer_utility(None)

                    if self.output_value == "":
                        self.output_value="00"

                    numbers = self.tokenize(self.output_value)
                    self.output_value=str(max(numbers))

                # --- Average ---    
                case"72":
                    self.lexer_utility(None)

                    if self.output_value == "":
                        self.output_value="00"

                    numbers = self.tokenize(self.output_value)
                    total = sum(map(int, numbers))
                    self.output_value=self.rounder(str(total//len(numbers)))

                # --- Sum ---   
                case"73":
                    self.lexer_utility(None)

                    if self.output_value == "":
                        self.output_value="00"
                        
                    numbers = self.tokenize(self.output_value)
                    total = sum(map(int, numbers))
                    self.output_value = self.rounder(str(total))

                # --- Len ---    
                case"74":
                    self.lexer_utility(None)

                    self.output_value=self.rounder(str(len(self.output_value)//2))

                # --- Sort ---    
                case"75":
                    self.lexer_utility(None)

                    if self.output_value == "":
                        self.output_value="00"

                    numbers = self.tokenize(self.output_value)
                    numbers.sort()
                    self.output_value="".join(numbers)

                # --- Any ---    
                case"76":
                    self.lexer_utility(None)

                    if self.output_value == "":
                        self.output_value="00"

                    numbers = self.tokenize(self.output_value)
                    self.output_value=random.choice(numbers)

                # --- All Same ---
                case"77":
                    self.lexer_utility(None)

                    if self.output_value == "":
                        self.output_value="00"

                    numbers = self.tokenize(self.output_value)
                    
                    if all(x == numbers[0] for x in numbers): 
                        self.output_value="01"
                        
                    else:
                        self.output_value="00"

                # --- Random ---    
                case"78":
                    self.lexer_utility(None)

                    if self.output_value == "":
                        self.output_value = "00"

                    numbers = self.tokenize(self.output_value)
                    self.output_value = self.rounder(str(random.randint(int(min(numbers)),int(max(numbers)))))

                # --- Most Common ---
                case"79":
                    self.lexer_utility(None)

                    if self.output_value == "":
                        self.output_value="00"

                    self.output_value = self.most_common(self.tokenize(self.output_value))

                # --- Shuffle ---    
                case"80":
                    self.lexer_utility(None)

                    if self.output_value == "":
                        self.output_value="00"

                    numbers = self.tokenize(self.output_value)
                    random.shuffle(numbers)
                    self.output_value="".join(numbers)

                # --- Reverse ---    
                case"81":
                    self.lexer_utility(None)

                    if self.output_value == "":
                        self.output_value="00"

                    numbers = self.tokenize(self.output_value)
                    numbers.reverse()
                    self.output_value="".join(numbers)
            
                case _:
                    if self.higher_tokenized_code==[]:
                        del self.tokenized_code[self.lindex][index+1+self.depth-deleted]
                        deleted+=1

                    else:
                        del self.higher_tokenized_code[self.higher_lindex][index+1+self.depth-deleted]
                        deleted+=1

        elif skip:
            skip=False

        index+=1
    
    self.lexer_utility(None)
    index=0

    if self.output_value!="":self.output.append(self.output_value)#If output value is not "", it will be added to output

    for self.output_value in self.output:#Checks for math in each part

        if any(symbol in self.output_value for symbol in self.math):#Checking for math
            self.output_value=self.output_value.replace("++","+").replace("--","-").replace("**","*").replace(">>",">").replace("<<","<").replace("&&","&").replace("||","|").replace("~~","~")#The math logic returns to its normal state
        
            try:#Tries to run math
                self.output_value = eval(re.sub(r'\b0+(\d+)', r'\1', self.output_value))#If math is found, it will try eval with removing excess 0

                if self.output_value < 0: 
                    self.output_value*=-1#ABS is applied as anything less than 0 doesn't exist :)

                if self.output_value == True: 
                    self.output_value = "01"

                if self.output_value == False: 
                    self.output_value = "00"

            except:
                self.output_value=None#If there's an error it will return empty string

        if self.output_value:
            self.output[index] = self.rounder(str(self.output_value))

        else:
            del self.output[index]
    
        index+=1 
        
    if self.output==[]:
        self.output=["00"]
        
    return(self.output) #Returns print value
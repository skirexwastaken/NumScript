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
    
    self.lexerOutputPart = ""
    self.lexerOutput = []

    self.variableByNumber = ""
    self.variableByVariable = ""

    self.indexByNumber = ""
    self.indexByVariable = ""

    self.stackByNumber = ""
    self.stackByVariable = ""

    # --- Building print value ---
    for token in range(tokensLength):
        
        # --- Skip is used to distinguish between pair and non pair tokens ---
        if not skip:

            # --- Match used to grab the current token ---    
            match tokens[index]:
            
                # --- Checking for number ---
                case"01":
                    self.lexerUtility(None)

                    self.lexerOutputPart+=tokens[index + 1]
                    skip=True

                # --- Checking for variable ---    
                case"02":
                    self.lexerUtility("cleanVariableByNumber")
                    
                    self.variableByNumber+=tokens[index + 1]
                    skip=True

                # --- Checking for variable with name being variable value ---
                case"03":
                    self.lexerUtility("cleanVariableByVariable")

                    self.variableByVariable += tokens[index + 1]
                    skip=True

                    # --- Grabs item by num index from the existing code ---    
                
                case"04":
                    self.lexerUtility("cleanIndexByNumber")

                    self.indexByNumber += tokens[index + 1]
                    skip=True

                # --- Grabs item by var index from the existing code ---    
                case"05":
                    self.lexerUtility("cleanIndexByVariable")

                    self.indexByVariable+=tokens[index + 1]
                    skip=True

                # --- Rest is num ---    
                case"06":
                    self.lexerUtility(None)

                    tokens=tokens[index+1:]
                    self.lexerOutputPart+= "".join(tokens[:-1])
                    break

                # --- Rest is var ---
                case"07":
                    self.lexerUtility(None)

                    tokens=tokens[index+1:]
                    self.variableByNumber+= "".join(tokens[:-1])
                    break

                # --- Call stack with num value ---
                case"08":
                    self.lexerUtility("cleanstackByNumber")

                    self.stackByNumber+=tokens[index + 1]
                    skip=True

                # --- Call stack with var value ---
                case"09":
                    self.lexerUtility("cleenstackByVariable")

                    self.stackByVariable+=tokens[index + 1]
                    skip=True

                # --- Input ---    
                case"12":
                    self.lexerUtility(None)

                    inputedCode = self.tokenizer(input(self.input_symbol).replace(" ",""))

                    if isinstance(inputedCode, list):
                        self.lexerOutputPart+= "".join(inputedCode)

                # --- Comment ---        
                case"22":
                    break

                # --- Checking for split between variable/variable ---            
                case"23":
                    self.variableByNumberCheck()

                # --- Checking for split between parts ---
                case"24":
                    self.lexerUtility(None)

                    self.lexerOutput.append(self.lexerOutputPart)
                    self.lexerOutputPart= ""

                # --- Adds day/month/year ---
                case"26":
                    self.lexerUtility(None)

                    now=datetime.now()
                    self.lexerOutputPart+= self.rounder(str(now.day)) + self.rounder(str(now.month)) + self.rounder(str(now.year))

                # --- Adds hour/minute ---   
                case"27":
                    self.lexerUtility(None)

                    now=datetime.now()
                    self.lexerOutputPart+= self.rounder(str(now.hour)) + self.rounder(str(now.minute))

                # --- Checking for math logic ---
                case"30"|"31"|"32"|"33"|"34"|"35"|"36"|"37"|"38"|"39":    
                    self.lexerUtility(None)

                    self.lexerOutputPart+={"30": "++", "31": "--", "32": "**", "33": "//", "34": ">>", "35": "<<", "36": "==", "37": "&&", "38": "||", "39": "~~"}[tokens[index]]
            
                # --- Min ---
                case"70":
                    self.lexerUtility(None)
                
                    if self.lexerOutputPart == "":
                        self.lexerOutputPart= "00"

                    numbers = self.tokenize(self.lexerOutputPart)

                    self.lexerOutputPart=str(min(self.onlyNumbers(numbers)))

                # --- Max ---    
                case"71":
                    self.lexerUtility(None)

                    if self.lexerOutputPart == "":
                        self.lexerOutputPart= "00"

                    numbers = self.tokenize(self.lexerOutputPart)

                    self.lexerOutputPart=str(max(self.onlyNumbers(numbers)))

                # --- Average ---    
                case"72":
                    self.lexerUtility(None)

                    if self.lexerOutputPart == "":
                        self.lexerOutputPart= "00"

                    numbers = self.tokenize(self.lexerOutputPart)
                    total = sum(map(int, self.onlyNumbers(numbers)))
                    self.lexerOutputPart=self.rounder(str(total // len(numbers)))

                # --- Sum ---   
                case"73":
                    self.lexerUtility(None)

                    if self.lexerOutputPart == "":
                        self.lexerOutputPart= "00"
                        
                    numbers = self.onlyNumbers(self.tokenize(self.lexerOutputPart))

                    total = 0

                    for number in numbers:
                        total += int(number)

                    self.lexerOutputPart = self.rounder(str(total))

                # --- Len ---    
                case"74":
                    self.lexerUtility(None)

                    self.lexerOutputPart=self.rounder(str(len(self.lexerOutputPart) // 2))

                # --- Sort ---    
                case"75":
                    self.lexerUtility(None)

                    if self.lexerOutputPart == "":
                        self.lexerOutputPart= "00"

                    numbers = self.tokenize(self.lexerOutputPart)
                    numbers.sort()
                    self.lexerOutputPart= "".join(numbers)

                # --- Any ---    
                case"76":
                    self.lexerUtility(None)

                    if self.lexerOutputPart == "":
                        self.lexerOutputPart= "00"

                    numbers = self.tokenize(self.lexerOutputPart)
                    self.lexerOutputPart=random.choice(self.onlyNumbers(numbers))

                # --- All Same ---
                case"77":
                    self.lexerUtility(None)

                    if self.lexerOutputPart == "":
                        self.lexerOutputPart= "00"

                    numbers = self.tokenize(self.lexerOutputPart)
                    
                    if all(x == numbers[0] for x in numbers): 
                        self.lexerOutputPart= "01"
                        
                    else:
                        self.lexerOutputPart= "00"

                # --- Random ---    
                case"78":
                    self.lexerUtility(None)

                    if self.lexerOutputPart == "":
                        self.lexerOutputPart = "00"

                    numbers = self.onlyNumbers(self.tokenize(self.lexerOutputPart))


                    self.lexerOutputPart = self.rounder(str(random.randint(int(min(numbers)), int(max(numbers)))))

                # --- Most Common ---
                case"79":
                    self.lexerUtility(None)

                    if self.lexerOutputPart == "":
                        self.lexerOutputPart= "00"

                    self.lexerOutputPart = self.mostCommon(self.tokenize(self.lexerOutputPart))

                # --- Shuffle ---    
                case"80":
                    self.lexerUtility(None)

                    if self.lexerOutputPart == "":
                        self.lexerOutputPart= "00"

                    numbers = self.tokenize(self.lexerOutputPart)
                    random.shuffle(numbers)
                    self.lexerOutputPart= "".join(numbers)

                # --- Reverse ---    
                case"81":
                    self.lexerUtility(None)

                    if self.lexerOutputPart == "":
                        self.lexerOutputPart= "00"

                    numbers = self.tokenize(self.lexerOutputPart)
                    numbers.reverse()
                    self.lexerOutputPart= "".join(numbers)
            
                case _:
                    if self.higherTokenizedCode == []:
                        del self.tokenizedCode[self.lindex][index + 1 + self.depth - deleted]
                        deleted += 1

                    else:
                        del self.higherTokenizedCode[self.higherLindex][index + 1 + self.depth - deleted]
                        deleted += 1

        else: skip=False

        index += 1
    
    self.lexerUtility(None)
    index=0

    if self.lexerOutputPart!= "":self.lexerOutput.append(self.lexerOutputPart)#If output value is not "", it will be added to output

    for self.lexerOutputPart in self.lexerOutput:#Checks for math in each part

        if any(symbol in self.lexerOutputPart for symbol in self.math):#Checking for math
            self.lexerOutputPart=self.lexerOutputPart.replace("++", "+").replace("--", "-").replace("**", "*").replace(">>", ">").replace("<<", "<").replace("&&", "&").replace("||", "|").replace("~~", "~")#The math logic returns to its normal state
        
            try:#Tries to run math
                self.lexerOutputPart = eval(re.sub(r'\b0+(\d+)', r'\1', self.lexerOutputPart))#If math is found, it will try eval with removing excess 0

                if self.lexerOutputPart < 0:
                    self.lexerOutputPart*=-1#ABS is applied as anything less than 0 doesn't exist :)

                if self.lexerOutputPart == True:
                    self.lexerOutputPart = "01"

                if self.lexerOutputPart == False:
                    self.lexerOutputPart = "00"

            except:
                self.lexerOutputPart=None#If there's an error it will return empty string

        if self.lexerOutputPart:
            self.lexerOutput[index] = self.rounder(str(self.lexerOutputPart))

        else:
            del self.lexerOutput[index]
    
        index += 1
        
    if self.lexerOutput==[]:
        self.lexerOutput=["00"]
        
    return(self.lexerOutput) #Returns print value
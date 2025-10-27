# --- Importing Libraries ---
import os
import time
import json
import time
import random

# --- Runs NS functions ---
def parser(self, tokens):
    
    # --- Checks if the code is to be added to definiton ---
    if tokens[0]=="57":
        if self.current_definition=="":
            self.current_definition="00"
            self.definitions[self.current_definition]=[]
            
        if self.current_definition not in self.definitions:
            self.definitions[self.current_definition]=[]
            
        if len(tokens[1:]) > 0:
            self.definitions[self.current_definition].append(tokens[1:])
        
        return("")
    
    else:
        self.current_definition=""
    
    # --- TAB ---
    if tokens[0]=="50":
        self.depth,index=0,0
        
        for token in tokens:
            if token=="50":
                self.depth += 1
                
            else:
                break
            
            index +=1
        tokens=tokens[index:]
        
        if self.depth>self.maxdepth:
            return("")
        
    else:
        self.depth,self.maxdepth=0,0
    
    # --- Checks for functions ---
    match tokens[0]:
        
        # --- Run ---
        case "00":
            builder = self.lexer(tokens)
            run_value = int("".join(builder))
            
            if self.higher_tokenized_code != []:
                if run_value < len(self.higher_tokenized_code):
                    self.line_runner([self.higher_tokenized_code[run_value]],0)  

                else:
                    return("-9900")

            else:
                if run_value < len(self.tokenized_code):
                    self.line_runner([self.tokenized_code[run_value]],0)

                else:
                    return("-9900")
        
        # --- Print ---
        case"10":
            return("".join(self.lexer(tokens)))
        
        # --- Print in NumScript Ascii ---
        case"11":
            return("".join([self.nsascii[chunk] for chunk in self.tokenize("".join(self.lexer(tokens)))]))
        
        # --- Define variable ---
        case"13":
            builder = self.lexer(tokens)

            while len(builder)<2:
                builder.append("00")

            var_name = builder[0]
            var_value = "".join(builder[1:])

            # --- Variable is added to variables ---
            self.variables[var_name] = str(var_value)

            return(f"-991323{var_name}23{var_value}")
        
        # --- Define pointer ---
        case"14":
            builder = self.lexer(tokens)

            while len(builder) < 2:
                builder.append("00")

            pointer_name,builder = builder[0],builder[1:]
            self.pointers[pointer_name] = []

            for variable in builder:
                if variable not in self.variables:
                    self.variables[variable]="00"

                self.pointers[pointer_name].append(variable)

            return("-991423"+"".join(builder))
        
        # --- Remove variable from pointer by name ---
        case"15":
            builder = self.lexer(tokens)

            while len(builder) < 2:
                builder.append("00")
            
            pointer_name = builder[0]
            variable_name = "".join(builder[1:])
            
            if pointer_name not in self.pointers:
                self.pointers[pointer_name]=[]
                return(f"-991523{pointer_name}")
            
            if variable_name in self.pointers[pointer_name]:
                del self.pointers[pointer_name][self.pointers[pointer_name].index(variable_name)]
                
            return(f"-991523{pointer_name}") 
        
        # --- Remove variable from pointer by index ---
        case"16":
            builder = self.lexer(tokens)

            while len(builder)<2:
                builder.append("00")

            pointer_name = builder[0]

            index = "".join(builder[1:])

            if pointer_name not in self.pointers:
                self.pointers[pointer_name]=[]
                return(f"-991623{pointer_name}")

            if not int(index) < len(self.pointers[pointer_name]):
                index = -1

            del self.pointers[pointer_name][int(index)]

            return(f"-991623{pointer_name}")
        
        # --- Append to pointer ---
        case"17":
            builder = self.lexer(tokens)

            while len(builder)<2:
                builder.append("00")

            name,builder = builder[0],builder[1:]

            if name not in self.pointers:
                self.pointers[name]=[]

            for variable in builder:

                if variable not in self.pointers[name]:
                    self.pointers[name].append(variable)

            return(f"-991723{name}")
        
        # --- Merge pointers ---
        case"18":
            builder=self.lexer(tokens)

            while len(builder) < 2:
                builder.append("00")

            first_pointer = builder[0]

            second_pointer = "".join(builder[1:])

            if first_pointer not in self.pointers:
                self.pointers[first_pointer]=[]

            if second_pointer not in self.pointers:
                self.pointers[second_pointer]=[]

            for i in self.pointers[second_pointer]:
                self.pointers[first_pointer].append(i)

            del self.pointers[second_pointer]

            name = "".join(self.pointers[first_pointer])

            return(f"-991823{name}")
        
        # --- Delete pointer --- 
        case"19":
            name = "".join(self.lexer(tokens))

            if name in self.pointers:
                del self.pointers[name]

            return(f"-991923{name}")
        
        # --- Exit ---
        case"20":
            if len(tokens) != 1:
                self.token_corrector()

            exit()
            
        # --- Restart ---    
        case"21":
            if len(tokens) != 1:
                self.token_corrector()

            os.system('cls' if os.name == 'nt' else 'clear')
            self.ascii_art()

            self.states = {"debug":False,"splitter":False,"print_tokens":False,"print_memory":False}

            self.lindex,self.tokenized_code= - 1,[]
            self.higher_lindex,self.higher_tokenized_code = -1,[]
 
            self.variables = {}
            self.definitions = {}
            self.pointers = {}

            return("-21")
        
        # --- Pass/Comment ---
        case"22":
            if len(tokens) != 1:
                self.token_corrector()

            return("")
        
        # --- Changes exe to read code from top to bottom ---
        case"28":
            if len(tokens) != 1:
                self.token_corrector()

            self.index_change=1

            return("-9928")
        
        # --- Changes exe to read code from bottom to top ---
        case"29":
            if len(tokens) != 1:
                self.token_corrector()

            self.index_change = -1

            return("-9929")
        
        # --- Jump ---
        case"40":
            if self.loop_callback==True:
                if self.maxdepth > 0:
                    self.maxdepth-=1

                self.loop_callback=False

            jump_value = "".join(self.lexer(tokens))

            if self.higher_tokenized_code == []:
                self.lindex = int(jump_value)-1

            else: 
                self.higher_lindex = int(jump_value)-1

            return(f"-994023{jump_value}")
        
        # --- Wait ---
        case"41":
            wait_value="".join(self.lexer(tokens))

            if int(wait_value) == 0:
                wait_value="01"

            time.sleep(int(wait_value))

            return(f"-994123{wait_value}") #Returns wait value
        
        # --- Clean console ---
        case"42":
            if len(tokens) != 1:
                self.token_corrector()    

            os.system('cls' if os.name == 'nt' else 'clear')
            self.ascii_art()

            return("-9942")
        
        # --- Clean states ---
        case"43":
            if len(tokens) != 1:
                self.token_corrector()

            self.states = {"debug":False,"splitter":False,"print_tokens":False,"print_memory":False}

            return("-9943")
        
        # --- Clean tokenized code ---
        case"44":
            if len(tokens) != 1:
                self.token_corrector()

            self.lindex,self.tokenized_code = -1,[]

            return("-9944")
        
        # --- Clean higher tokenized code ---
        case"45":
            if len(tokens) != 1:
                self.token_corrector()

            self.higher_lindex,self.higher_tokenized_code = -1,[]

            return("-9945")
        
        # --- Clean variables ---
        case"46":
            if len(tokens) != 1:
                self.token_corrector()

            self.variables = {}

            return("-9946")
        
        # --- Clean definitions ---
        case"47":
            if len(tokens) != 1:
                self.token_corrector()

            self.definitions = {}

            return("-9947")
        
        # --- Clean pointers ---
        case"48":
            if len(tokens) != 1:
                self.token_corrector()

            self.pointers = {}

            return("-9948")
        
        # --- Switching states ---
        case"49":
            tokens,index = tokens[1:],0

            if len(tokens) > 4:
                tokens[3] += "".join(tokens[4:])

            while len(tokens) < 4:
                tokens.append("00")

            for i in tokens:
                if i not in ["00","01"]:
                    if int(i) != 0:
                        tokens[index] = "01"

                    else:
                        tokens[index] = "00"

            keys = ["debug", "splitter", "print_tokens", "print_memory"]

            for i, key in enumerate(keys):
                self.states[key] = tokens[i] == "01"

            return("-49"+"".join(tokens))
        
        # --- Break ---
        case"51":
            if len(tokens) != 1:
                self.token_corrector()
                
            if self.depth > 0:
                self.depth -= 1

            if self.maxdepth > 0:
                self.maxdepth -= 1

            return("-9951")
        
        # --- If ---
        case"52":
            for i in self.lexer(tokens):
                if i == "00":return("-995200")

            self.maxdepth += 1
            self.loop_callback=True

            return("-995201")
        
        # --- While loop ---
        case"53":
            for i in self.lexer(tokens):
                if i == "00":
                    return("-995300")
                
            self.maxdepth += 1
            if self.higher_tokenized_code != []:
                temp_higher_lindex = self.higher_lindex

                for i in self.higher_tokenized_code[self.higher_lindex:]:
                    if len(i) < self.depth+1:
                        self.maxdepth -= 1
                        break

                    i = i[self.depth+1:]
                    if i[0] == "51":
                        jump_part=["40","01",self.rounder(str(self.higher_lindex))]

                        for i in range(self.depth+1):
                            jump_part.insert(0,"50")

                        self.higher_tokenized_code[temp_higher_lindex] = jump_part

                        break

                    temp_higher_lindex+=1

                self.higher_tokenized_code[self.higher_lindex][self.depth] = "52"
            else:
                temp_lindex=self.lindex
                for i in self.tokenized_code[self.lindex:]:
                    if len(i) < self.depth+1:
                        self.maxdepth -= 1
                        break

                    i = i[self.depth+1:]
                    if i[0] == "51":
                        jump_part=["40","01",self.rounder(str(self.lindex))]

                        for i in range(self.depth+1):
                            jump_part.insert(0,"50")

                        self.tokenized_code[temp_lindex]=jump_part

                        break

                    temp_lindex += 1

                self.tokenized_code[self.lindex][self.depth] = "52"

            self.loop_callback = True

            return("-995301")
        
        # --- For loop ---
        case"54":
            if_value = "".join(self.lexer(tokens))

            if if_value not in self.variables:
                self.variables[if_value] = "00"

            if self.variables[if_value] == "00":
                return("-995400")
            
            self.maxdepth += 1

            if self.higher_tokenized_code != []:
                temp_higher_lindex=self.higher_lindex

                for i in self.higher_tokenized_code[self.higher_lindex:]:
                    if len(i) < self.depth+1:
                        self.maxdepth -= 1
                        break

                    i = i[self.depth+1:]

                    if i[0] == "51":
                        jump_part=["40","01",self.rounder(str(self.higher_lindex))]
                        var_define_part=["13","01",self.rounder(str(if_value)),"24","02",self.rounder(str(if_value)),"31","01","01"]

                        for i in range(self.depth+1):
                            jump_part.insert(0,"50")
                            var_define_part.insert(0,"50")

                        self.higher_tokenized_code.insert(temp_higher_lindex, var_define_part)
                        self.higher_tokenized_code.insert(temp_higher_lindex + 1, jump_part)

                        break

                    temp_higher_lindex += 1
                if_part=["52","01","00","35","02",self.rounder(str(if_value))]

                for i in range(self.depth):
                    if_part.insert(0,"50")

                self.higher_tokenized_code[self.higher_lindex] = if_part

            else:
                temp_lindex=self.lindex
                for i in self.tokenized_code[self.lindex:]:
                    if len(i) < self.depth+1:
                        self.maxdepth -= 1
                        break

                    i = i[self.depth+1:]


                    if i[0]=="51":
                        jump_part=["40","01",self.rounder(str(self.lindex))]
                        var_define_part=["13","01",self.rounder(str(if_value)),"24","02",self.rounder(str(if_value)),"31","01","01"]

                        for i in range(self.depth+1):
                            jump_part.insert(0,"50")
                            var_define_part.insert(0,"50")

                        self.tokenized_code.insert(temp_lindex, var_define_part)
                        self.tokenized_code.insert(temp_lindex + 1, jump_part)

                        break

                    temp_lindex += 1

                if_part=["52","01","00","35","02",self.rounder(str(if_value))]

                for i in range(self.depth):
                    if_part.insert(0,"50")

                self.tokenized_code[self.lindex] = if_part

            self.loop_callback = True

            return("-995401")
        
        # --- Do if ---
        case"55":
            if self.higher_tokenized_code != []:
                self.higher_tokenized_code[self.higher_lindex][0+self.depth] = "52"

            else:
                self.tokenized_code[self.lindex][0+self.depth] = "52"

            return("-9955")
        
        # --- Define ---
        case"56":
            self.current_definition = "".join(self.lexer(tokens))
            
            self.definitions[self.current_definition] = []
            
            return(f"-995623{self.current_definition}")
        
        # --- Call definition ---
        case"58":
            definition_name = "".join(self.lexer(tokens))
            
            if definition_name not in self.definitions:
                self.definitions[definition_name] = []

                return("-995800")
            
            else:
                temp_higher_lindex = self.higher_lindex
                                    
                for line in self.definitions[definition_name]:    
                    self.higher_tokenized_code.insert(temp_higher_lindex+1,line)
                    temp_higher_lindex+=1
                    
                return(f"-995823{definition_name}")
            
        # --- Lambda ---    
        case"59":
            definition_builder = self.lexer(tokens)
            
            while len(definition_builder)<2:
                definition_builder.append("00")
            
            definition_name = definition_builder[0]
            
            definition_code = "".join(definition_builder[1:])
            definition_code=self.tokenize(definition_code)
            
            self.definitions[definition_name] = [definition_code]
            
            return(f"-99{definition_name}23{definition_code}")
        
        # --- Load TXT ---
        case"60": 
            builder = self.lexer(tokens)

            while len(builder) < 2:
                builder.append("00")

            var_name=builder[0]
            if var_name not in self.variables:
                self.variables[var_name] = "00"

            filename = "".join(builder[1:])

            try:
                with open(f"Data/Files/{filename}.txt","r") as file:
                    lines=file.readlines()
                    self.variables[var_name]=""   
                    parts = []

                    for line in lines:
                        line = line.rstrip('\n')

                        for letter in line:
                            parts.append(self.reversed_nsascii.get(letter, "00"))
                            self.variables[var_name] = "".join(parts)  

                    return(f"-9960{filename}")
            except:

                return("-996000")
        
        # --- Save TXT ---
        case"61":
            builder=self.lexer(tokens)

            while len(builder) < 2:
                builder.append("00")

            var_name=builder[0]
            if var_name not in self.variables:
                self.variables[var_name]="00"

            filename="".join(builder[1:])

            with open(f"Data/Files/{filename}.txt","w") as file:
                file.write(self.variables[var_name])

            return("-9961")
        
        # --- Save TXT in NumScript Ascii ---
        case"62":
            builder=self.lexer(tokens)

            while len(builder) < 2:
                builder.append("00")

            var_name=builder[0]
            if var_name not in self.variables:
                self.variables[var_name]="00"

            filename="".join(builder[1:])

            with open(f"Data/Files/{filename}.txt","w") as file:
                var_value=""

                for i in self.tokenize(self.variables[var_name]):
                    var_value+=self.nsascii[i]

                file.write(var_value)

            return("-9962")
        
        # --- Import variables ---
        case"63":
            builder = self.lexer(tokens)

            while len(builder)<2:
                builder.append("00")

            filename = builder[0]
            variable_names = builder[1:]

            try:
                with open("Data/Variables/"+filename+".json","r") as file:
                    data=json.load(file)

            except:
                return("-996300")
            
            for variable in variable_names:

                if variable not in data:
                    data[i]="00"

                self.variables[variable]=data[variable]
                
            output="23".join(variable_names)

            return(f"-9963{output}")
        
        # --- Export variables ---
        case"64":
            name_var = self.lexer(tokens)

            while len(name_var)<2:
                name_var.append("00")

            filename = name_var[0]
            name_var = name_var[1:]
            save = {}

            for i in name_var:
                if i not in self.variables:
                    self.variables[i]="00"

                save[i]=self.variables[i]

            with open("Data/Variables/"+filename+".json","w") as file:
                json.dump(save,file)

            output=""

            for i in name_var:
                output+="23"+i

            return(f"-9964{output}")
        
        # --- Import pointers --- 
        case"65":
            name_pointers = self.lexer(tokens)

            while len(name_pointers)<2:
                name_pointers.append("00")

            filename = name_pointers[0]
            name_pointers = name_pointers[1:]

            try:
                with open("Data/Pointers/"+filename+".json","r") as file:
                    data=json.load(file)

            except:
                return("-996500")
            
            for i in name_pointers:

                if i not in data:
                    data[i]=["00"]

                self.pointers[i]=data[i]

            output = "23"+"23".join(name_pointers)

            return(f"-9965{output}")
        
        # --- Export pointers ---
        case"66":
            name_pointers= self.lexer(tokens)

            while len(name_pointers) < 2:
                name_pointers.append("00")

            filename = name_pointers[0]
            name_pointers = name_pointers[1:]
            save = {}

            for i in name_pointers:
                if i not in self.pointers:
                    self.pointers[i]=[]

                save[i] = self.pointers[i]

            with open("Data/Pointers/"+filename+".json","w") as file:
                json.dump(save,file)

            output = "23".join(name_pointers)

            return(f"-996623{output}")
        
        # --- Import Definition --- 
        case"67":
            name_def= self.lexer(tokens)
            
            while len(name_def)<2:
                name_def.append("00")

            filename = name_def[0]
            name_def = name_def[1:]

            try:
                with open("Data/Definitions/"+filename+".json","r") as file:data=json.load(file)

            except:
                return("-996700")
            
            for i in name_def:

                if i not in data:
                    data[i]=[]

                self.definitions[i]=data[i]

            output = "23".join(name_def)

            return(f"-996723{output}")
        
        # --- Export Definition ---
        case"68":
            name_def= self.lexer(tokens)

            while len(name_def) < 2:
                name_def.append("00")

            filename = name_def[0]
            name_def = name_def[1:]
            save = {}

            for i in name_def:
                if i not in self.definitions:
                    self.definitions[i]=[]

                save[i] = self.definitions[i]

            with open("Data/Definitions/"+filename+".json","w") as file:
                json.dump(save,file)

            output="23".join(name_def)

            return(f"-996823{output}")
        
        # --- Load NS code from other file into higher tokenized code ---
        case"69":
            filename_input = self.lexer(tokens)

            filename = "".join(filename_input)

            try:
                with open("Data/Code/"+filename+".ns", 'r', encoding='utf-8') as file:lines = [line.rstrip('\n') for line in file]

            except:
                return("-996900")
            
            temp_higher_lindex=self.higher_lindex

            for i in lines:
                i = self.tokenizer(i.replace(" ",""))

                if isinstance(i, list):
                    self.higher_tokenized_code.insert(temp_higher_lindex,i)
                    temp_higher_lindex += 1
                    
            return(f"-996923{filename}")
        
        # --- Poke variables name by index ---
        case"82":
            variables_index_str = "".join(self.lexer(tokens))

            try:
                int_index = int(variables_index_str)
                var_names = list(self.variables.keys())

                if 0 <= int_index < len(var_names):
                    return(f"8223{var_names[int_index]}")

                else:
                    return("-822300")

            except:
                return("-822300")
            
        # --- Poke variables value by index ---     
        case"83":
            self.variables_index_str = "".join(self.lexer(tokens))

            try:
                int_index = int(self.variables_index_str)
                var_values = list(self.variables.values())

                if 0 <= int_index < len(var_values):
                    return(f"8323{var_values[int_index]}")
                
                else:
                    return("-832300")
                
            except:
                return("-832300")
            
        # --- Insert to tokenized code ---    
        case"84":
            code = self.lexer(tokens)

            while len(code) < 2:
                code.append("00")

            index = int(code[0])
            code = code[1:]
            line = "".join(code)

            lines = self.compiler([self.tokenize(line)])
            lines = self.compiler(lines)

            for line in lines:
                self.tokenized_code.insert(index,line)
                index += 1
            return("-9984")
        
        # --- Insert to higher tokenized code ---
        case"85":
            code = self.lexer(tokens)

            while len(code) < 2:
                code.append("00")

            index = int(code[0])
            code = code[1:]
            line = "".join(code)
            self.higher_tokenized_code.insert(index,self.tokenize(line))

            return("-9985")
        
        # --- Remove variable from variables ---
        case"86":
            var_names = self.lexer(tokens)

            for var_name in var_names:

                if var_name in self.variables:
                    del self.variables[var_name]

            return("-9986")
        
        # --- Remove definition from variables ---
        case"87":
            def_names = self.lexer(tokens)

            for def_name in def_names:

                if def_name in self.definitions:
                    del self.definitions[def_name]

            return("-9987")
        
        # --- Swap variable name with value ---
        case"88":
            var_name = self.lexer(tokens)

            if var_name == []:
                var_name.append("00")

            var_name = "".join(var_name)

            if var_name not in self.variables:
                self.variables[var_name]="00"

            var_value = self.variables[var_name]
            del self.variables[var_name]
            self.variables[var_value] = var_name

            return(f"-9988{var_value}23{var_name}")
        
        # --- Rename variable ---
        case"89":
            builder = self.lexer(tokens)

            old_name = builder[0]
            builder = builder[1:]
            new_name = "".join(builder)

            if old_name in self.variables:
                value = self.variables[old_name]
                del self.variables[old_name]

            else:
                value = "00"
                
            self.variables[new_name] = value

            return(f"-9989{new_name}23{value}")
        
        # --- Contains ---
        case"90":
            builder = self.lexer(tokens)

            while len(builder)<3:
                builder.append("00")

            contains = builder[0]
            variable = builder[1]

            if variable not in self.variables:
                self.variables[variable]="00"

            builder = builder[2:]
            str_builder = "".join(builder)
            builder = self.tokenize(str_builder)

            if contains in builder:
                self.variables[variable]="01";return("902301")
            
            else:self.variables[variable]="00";return("902300")
            
        # --- Add token by index ---    
        case"91":
            builder = self.lexer(tokens)

            while len(builder)<3:
                builder.append("00")

            var_name,index = builder[0],builder[1]
            builder = builder[2:]
            expansion = "".join(builder)

            if var_name not in self.variables:
                self.variables[var_name]="00"

            var_value = self.variables[var_name]
            numbers = self.tokenize(var_value)

            if not(0 <= int(index) < len(numbers)):
                index = -1

            numbers.insert(int(index),expansion)
            var_value = "".join(numbers)
            var_value = self.rounder(var_value)
            self.variables[var_name]=var_value

            return(f"-9991{var_name}23{var_value}")
        
        # --- Remove token by index ---
        case"92":
            builder = self.lexer(tokens)

            while len(builder)<2:
                builder.append("00")

            var_name = builder[0]
            builder = builder[1:]
            index = "".join(builder)

            if var_name not in self.variables:
                self.variables[var_name]=="00"

            var_value = self.variables[var_name]
            numbers = self.tokenize(var_value)

            if not(0 <= int(index) < len(numbers)):
                index = -1

            del numbers[int(index)]
            var_value="".join(numbers)

            if var_value == "":
                var_value = "00"

            var_value = self.rounder(var_value)
            self.variables[var_name] = var_value

            return(f"-9992{var_name}23{var_value}")
        
        # --- Replace ---
        case"93":
            builder = self.lexer(tokens)

            while len(builder)<4:
                builder.append("00")

            var_name,original_token,new_token = builder[0],builder[1],builder[2]

            if var_name not in self.variables:
                self.variables[var_name]="00"

            str_builder = "".join(builder[3:])
            builder = str_builder.replace(original_token,new_token)
            self.variables[var_name] = builder

            return(f"-999323{builder}")
        
        # --- Replace by index ---
        case"94":
            builder = self.lexer(tokens)

            while len(builder)<3:
                builder.append("00")

            var,idx = builder[0],builder[1]
            token = "".join(builder[2:])

            if var not in self.variables:
                self.variables[var] = "00"

            var_value = self.tokenize(self.variables[var])
            
            if not(0 <= int(idx) < len(var_value)):
                idx = -1

            var_value[int(idx)]=token
            self.variables[var] = "".join(var_value)

            return(f"-999423{self.variables[var]}")
        
        # --- Random randint ---
        case"95":
            builder = self.lexer(tokens)

            while len(builder) < 3:
                builder.append("00")

            var,min = builder[0],builder[1]
            max = "".join(builder[2:])
            self.variables[var] = self.rounder(str(random.randint(int(min),int(max))))

            return(f"-999523{self.variables[var]}")
        
        # --- Sub string (extracts part of string by start and end) ---
        case"96":
            builder = self.lexer(tokens)

            while len(builder) < 3:
                builder.append("00")

            var_name = builder[0]
            start = int(builder[1])
            end = int("".join(builder[2:]))

            if var_name not in self.variables:
                self.variables[var_name] = "00"

            var_value = self.variables[var_name]

            if start > len(var_value):
                start = 0

            if end > len(var_value):
                end = -1

            var_value = self.tokenize(var_value)[start::end]
            var_value = "".join(var_value)
            self.variables[var_name] = var_value
            
            return(f"-999623{var_value}")
        
        # --- &= -> if variable value is same as inputed value, the variable is set to 01, else 00 ---
        case"97":
            builder = self.lexer(tokens)

            while len(builder)<2:
                builder.append("00")

            var_name = builder[0]
            builder = builder[1:]
            value = "".join(builder)

            if var_name not in self.variables:
                self.variables[var_name] = "00"

            if var_name == value:
                self.variables[var_name] = "01"

            else:
                self.variables[var_name] = "00"

            return(f"-999723{self.variables[var_name]}")
        
        # --- |= -> if variable value is not same as inputed value, the variable is set to 00, else 01 ---
        case"98":
            builder = self.lexer(tokens)

            while len(builder)<2:
                builder.append("00")

            var_name = builder[0]
            value = "".join(builder[1:])

            if var_name not in self.variables:
                self.variables[var_name] = "00"

            if var_name != value:
                self.variables[var_name] = "01"

            else:
                self.variables[var_name] = "00"

            return(f"-999823{self.variables[var_name]}")
        
        # --- Project guide ---  
        case"99":
            if len(tokens) != 1:
                self.token_corrector()

            return("https://numscript.xyz/")
        
        # --- Invalid function -> Line gets deleted ---
        case _:
            if self.higher_tokenized_code == []:
                del self.tokenized_code[self.lindex]
                self.lindex-=self.index_change

            else:
                del self.higher_tokenized_code[self.higher_lindex]
                self.higher_lindex-=self.index_change
# --- Runs code in tokenized and higer tokenized variables --- 
def run(self):
    # --- Removing THEN from both tokenized codes ---
    self.tokenized_code = self.compiler(self.tokenized_code)
    
    # --- Running code --- 
    while self.lindex < len(self.tokenized_code):#Tokenized code has lower priority than higher tokenized code, so if new tokens are added to higher tokenized code durring the procces of running tokenized code, exe() will switch to executing higher tokenized code
        self.line_runner(self.tokenized_code,self.lindex)#Runs tokenized code
        if self.lindex+self.index_change >= 0:#If index + index change is not negative
            self.lindex+=self.index_change#index change is added to index

        else:
            self.lindex=len(self.tokenized_code)#If index + index_change would be negative, the exe process is stopped

        if self.higher_tokenized_code != []:#Checks if higher code isn't empty
            self.higher_tokenized_code = self.compiler(self.higher_tokenized_code)

            while self.higher_lindex != len(self.higher_tokenized_code):#Running higer tokenized code
                self.line_runner(self.higher_tokenized_code,self.higher_lindex)#Runs higher tokenized code

                if self.higher_lindex+self.index_change >= 0:#If index + index change is not negative
                    self.higher_lindex+=self.index_change#index change is added to index

                else:
                    self.higher_lindex=len(self.higher_tokenized_code)#If index + index_change would be negative, the exe process is stopped

            self.higher_tokenized_code,self.higher_lindex=[],0#Higher tokenized code and higher lindex are set to their default values
            
    # --- Setting state variables to their default values ---        
    self.tokenized_code = []
    self.lindex = 0
    self.maxdepth = 0
    self.depth = 0  
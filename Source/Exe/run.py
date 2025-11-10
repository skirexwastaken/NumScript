# --- Runs code in tokenized and higer tokenized variables --- 
def run(self):
    # --- Removing THEN from tokenized code ---
    self.tokenized_code = self.compiler(self.tokenized_code)
    
    """
    The idea here is that tokenized code has lower priority than higher tokenized code.
    The reason behind this is that for example called function needs to be executed instantly so its added to higher tokenized cody which has higher priority.
    """

    # --- Running tokenized code --- 
    while self.lindex < len(self.tokenized_code):
        
        # --- Line is passed to line_runner ---
        self.line_runner(self.tokenized_code,self.lindex)
        
        # --- If index change is valid ---
        if self.lindex+self.index_change >= 0:
            self.lindex+=self.index_change

        # --- If the index change would lead to selecting line before 0 or after end of file, the execution of tokenized code is stopped ---
        else:
            self.lindex=len(self.tokenized_code)

        # --- Checking if higher tokenized code is not empty ---
        if self.higher_tokenized_code != []:

            # --- Removing THEN from higher tokenized code ---
            self.higher_tokenized_code = self.compiler(self.higher_tokenized_code)

            # --- Running higher tokenized code ---
            while self.higher_lindex != len(self.higher_tokenized_code):

                # --- Line is passed to line runner ---
                self.line_runner(self.higher_tokenized_code,self.higher_lindex)

                # --- If index change is valid ---
                if self.higher_lindex+self.index_change >= 0:
                    self.higher_lindex+=self.index_change

                # --- If the index change would lead to selecting line before 0 or after end of file, the execution of higher tokenized code is stopped ---
                else:
                    self.higher_lindex=len(self.higher_tokenized_code)

            # --- After all of higher tokenized code is executed the variables tied to running it are set to their default values ---
            self.higher_tokenized_code = []
            self.higher_lindex = 0
            
    # --- Setting variables tied to code running to their default values ---        
    self.tokenized_code = []
    self.lindex = 0
    self.maxdepth = 0
    self.depth = 0  
# --- Corrects wrong tokens  ---
def token_corrector(self):

    if self.higher_tokenized_code:
        line=self.higher_tokenized_code[self.higher_lindex]
        self.higher_tokenized_code[self.higher_lindex]=line[:-len(line)+self.depth+1]

    else:
        line=self.tokenized_code[self.lindex]
        self.tokenized_code[self.lindex]=line[:-len(line)+self.depth+1]
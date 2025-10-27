# --- Makes sure proper token format is kept at output ---
def rounder(self, output):
    if len(output)%2==1: 
        return"0"+output
    
    return(output)
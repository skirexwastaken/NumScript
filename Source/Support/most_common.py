# --- Importing Libraries ---
from collections import Counter

# --- Checks for the most common item ---
def most_common(self, lst):
    if not lst: 
        return None
    
    return Counter(lst).most_common(1)[0][0]
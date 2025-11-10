# --- Importing Libraries ---
import json
import types
import os

# --- NumScript Virtual Machine ---
class NumScriptVirtualMachine():
    
    # --- Setup of "Global Variables" ---
    def __init__(self):
        
        # --- Defining Global Variables ---
        self.math = ["++", "--", "**", "//", ">>", "<<", "==", "&&", "||", "~~"]#List of all math symbols, used in lexer
        self.nsascii = {"00": "a", "01": "b", "02": "c", "03": "d", "04": "e", "05": "f", "06": "g", "07": "h", "08": "i", "09": "j","10": "k", "11": "l", "12": "m", "13": "n", "14": "o", "15": "p", "16": "q", "17": "r", "18": "s", "19": "t","20": "u", "21": "v", "22": "w", "23": "x", "24": "y", "25": "z", "26": "A", "27": "B", "28": "C", "29": "D","30": "E", "31": "F", "32": "G", "33": "H", "34": "I", "35": "J", "36": "K", "37": "L", "38": "M", "39": "N","40": "O", "41": "P", "42": "Q", "43": "R", "44": "S", "45": "T", "46": "U", "47": "V", "48": "W", "49": "X","50": "Y", "51": "Z", "52": "0", "53": "1", "54": "2", "55": "3", "56": "4", "57": "5", "58": "6", "59": "7","60": "8", "61": "9", "62": "!", "63": "\"", "64": "#", "65": "$", "66": "%", "67": "&", "68": "'", "69": "(","70": ")", "71": "*", "72": "+", "73": ",", "74": "-", "75": ".", "76": "/", "77": ":", "78": ";", "79": "<","80": "=", "81": ">", "82": "?", "83": "@", "84": "[", "85": "\\", "86": "]", "87": "^", "88": "_", "89": "`","90": "{", "91": "|", "92": "}", "93": "~", "94": "€", "95": "£", "96": "¥", "97": "¢", "98": "§", "99": " "}
        self.reversed_nsascii = {"a": "00", "b": "01", "c": "02", "d": "03", "e": "04", "f": "05", "g": "06", "h": "07", "i": "08", "j": "09","k": "10", "l": "11", "m": "12", "n": "13", "o": "14", "p": "15", "q": "16", "r": "17", "s": "18", "t": "19","u": "20", "v": "21", "w": "22", "x": "23", "y": "24", "z": "25", "A": "26", "B": "27", "C": "28", "D": "29","E": "30", "F": "31", "G": "32", "H": "33", "I": "34", "J": "35", "K": "36", "L": "37", "M": "38", "N": "39","O": "40", "P": "41", "Q": "42", "R": "43", "S": "44", "T": "45", "U": "46", "V": "47", "W": "48", "X": "49","Y": "50", "Z": "51", "0": "52", "1": "53", "2": "54", "3": "55", "4": "56", "5": "57", "6": "58", "7": "59","8": "60", "9": "61", "!": "62", """: "63", "#": "64", "$": "65", "%": "66", "&": "67", """: "68", "(": "69",")": "70", "*": "71", "+": "72", ",": "73", "-": "74", ".": "75", "/": "76", ":": "77", ";": "78", "<": "79","=": "80", ">": "81", "?": "82", "@": "83", "[": "84", "\\": "85", "]": "86", "^": "87", "_": "88", "`": "89","{": "90", "|": "91", "}": "92", "~": "93", "€": "94", "£": "95", "¥": "96", "¢": "97", "§": "98", " ": "99"}

        self.index_change=1#Defines if code is red from top to bottom or from bottom to top

        self.lindex = 0#Tokenized code index, specifies which line of code is currently interpreted
        self.higher_lindex = 0#Higher tokenized code index, specifies which line of code is currently interpreted

        self.tokenized_code = []#Tokenized code
        self.higher_tokenized_code = []#Tokenized code with higher priority

        self.depth = 0#Depth when it comes to conditional statements/loops
        self.maxdepth = 0#Max depth when it comes to conditional statements/loops

        self.variables = {}#Variable variables
        self.pointers = {}#Pointer variables
        self.definitions = {}#Definitions variables

        self.current_definition = ""#Current definiton that is being defined

        self.loop_callback = False#Helper variable for loops
        
        # --- Checking if Data folders exist ---
        for folder in ["Code","Definitions","Files","Pointers","Variables"]:
            if not os.path.exists(f"Data/{folder}"):
                os.makedirs(f"Data/{folder}")
        
        # --- Settings of Interpreter ---
        with open("Source/JSON/settings.json","r") as settings_file:
            settings = json.load(settings_file)
            
            self.states = settings["states"]
        
            self.shell_in_symbol = settings["symbols"]["shell_in"]
            self.shell_out_symbol = settings["symbols"]["shell_out"]
            self.input_symbol = settings["symbols"]["input"]

        # --- Importing modules ---
        with open("Source/JSON/module_paths.json","r") as module_paths_file:
            modules_to_import = json.load(module_paths_file)

            for module_path, function_name in modules_to_import.items():
                module = __import__(f"Source.{module_path}", fromlist=[function_name])
                func = getattr(module, function_name)
                setattr(self, function_name, types.MethodType(func, self))
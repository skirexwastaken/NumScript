# NumScript: A numerical programming language

> NumScript is a lightweight, esoteric, interpreted scripting language designed for numerical programming and writing simple scripts.

> The language started as a joke back in middle of the 2024 and over time it grew into its current form featuring rich syntax.

> You can try the language and see a bigger guide at numscript.xyz

## Key Features

> Token-Based Syntax: All instructions are built using numeric token pairs (e.g., 13, 01)..

> Zero-Error Policy: NumScript never crashes. Mistyped or incomplete code will default to safe (though potentially unintended) behavior.

> Real-Time Execution: The interpreter processes code one line at a time with immediate feedback.

> Simplicity: NumScript features a minimalistic syntax and a limited set of data types, resulting in a lightweight and fast programming experience.

## Core Mechanics

> NumScript is an interpreted language, meaning the interpreter reads and executes the code one line at a time.

> The code is first processed by a tokenizer, which verifies that its content is numeric and splits it into token pairs, for example 10-01-00.

> After the instruction 00 (RUN) is passed, the code is firstly compiled to simplier format and is passed to the executor.

> Executor reads one line at a time and passes it to the code runner.

> Code runner passes the line into the parser.

> Parser analyzes the tokens to determine which function should be executed. This is defined by the first token pair.

> The first token pair is then removed, and the remaining tokens are passed to the lexer, which analyzes their content.

> The lexer outputs Lexer Blocks, which are groups of tokens representing final values. In code, these blocks are separated by the token 24.

> A good example of blocks is a variable definition: 13 01 00 24 01 01 01 00
    -> This expression contains two blocks: the first defines the variable name, and the second defines its value. The value of the first block is 00, and the value of the second block is 01 10.
    -> These blocks are then used as parameters in the functions being executed. When debugging is enabled, you can view each of these blocks in detail.

> After Lexer finishes analyzing all of the tokens, the rusulting Lexer Blocks are returned to Parser.

> Parser then sets the individual blocks as the parameters of the function that is being executed and the result is printed to console.

## Token MAP

| Name | Token | Description | Example |
|------|--------|-------------|----------|
| Run | 00 | Another way of running code inserted to console. | 00 |
| Number | 01 | Pointer towards a number. | 01 00 |
| Variable (num) | 02 | Pointer towards variable by name. | 02 00|
| Variable (var) | 03 | Points to variable by value of variable. | 03 00|
| Index (num) | 04 | Replaces lexer block by numeric index. | 01 00 01 01 04 00 |
| Index (var) | 05 | Replaces lexer block by variable value index. | 01 00 01 01 05 00 |
| Rest is num | 06 | Considers rest of line to be a number. | 06 00 01 |
| Rest is var | 07 | Considers rest of line to be a variable. | 07 00 01 |
| Pointer (num) | 08 | Calls all variables from a pointer where its name is a number. | 08 00 |
| Pointer (var) | 09 | Calls all variables from a pointer where its name is a variable value. | 09 00 |
| Print | 10 | Prints all lexer blocks. | 10 01 00 |
| Print in NS Ascii | 11 | Prints all lexer blocks translated by NS Ascii. | 11 01 00 |
| Input | 12 | Adds user input to current lexer block. | 10 12 |
| Let | 13 | Defines a variable (name + combined value). | 13 01 00 24 01 10 |
| Define pointer | 14 | Defines a pointer with listed variables. | 14 01 00 24 01 05 24 01 07 |
| Remove variable from pointer by name | 15 | Removes specific variables from pointer. | 15 01 00 24 01 05 |
| Remove variable from pointer by index | 16 | Removes specific variable from pointer by index. | 16 01 00 24 01 05 |
| Append to pointer | 17 | Adds variables to pointer. | 17 01 00 24 01 00 |
| Merge Pointers | 18 | Merges second pointer into first. | 18 01 00 24 01 01 |
| Delete pointer | 19 | Deletes specific pointer. | 19 01 00 |
| Exit | 20 | Ends execution of script. | 20 |
| Restart | 21 | Restarts the console. | 21 |
| Comment | 22 | Marks code as comment (not executed). | 22 10 01 00 |
| Split between variables | 23 | Splits between variables in lexer block. | 10 02 00 23 02 01 |
| Split in lexer parts | 24 | Split between lexer blocks. | 13 01 00 24 01 00 |
| Then | 25 | Allows multiple lines on one line. | 10 01 00 25 10 01 01 |
| Date | 26 | Inserts current date as number. | 10 26 |
| Time | 27 | Inserts current time as number. | 10 27 |
| Read down | 28 | Interpreter reads from top to bottom. | 28 |
| Read up | 29 | Interpreter reads from bottom to top. | 29 |
| + | 30 | Plus operator. | 10 01 01 30 01 01 |
| - | 31 | Minus operator. | 10 01 01 31 01 01 |
| * | 32 | Times operator. | 10 01 01 32 01 01 |
| / | 33 | Division operator. | 10 01 01 33 01 01 |
| > | 34 | Greater than operator. | 10 01 00 34 01 01 |
| < | 35 | Smaller than operator. | 10 01 01 35 01 01 |
| = | 36 | Equals operator. | 10 01 01 36 01 01 |
| & | 37 | AND operator. | 10 01 01 37 01 01 |
| \| | 38 | OR operator. | 10 01 01 38 01 01 |
| ~ | 39 | NOT operator. | 10 39 01 01 |
| Jump | 40 | Jumps to specific line. | 40 01 00 |
| Wait | 41 | Freezes script for time. | 41 01 01 |
| Clean Console | 42 | Cleans console content. | 42 |
| Clean States | 43 | Resets state values. | 43 |
| Clean Tokenized Code | 44 | Clears tokenized code. | 44 |
| Clean Higher Priority Tokenized Code | 45 | Clears higher priority tokenized code. | 45 |
| Clean Variables | 46 | Clears variable memory. | 46 |
| Clean Definitions | 47 | Clears definitions memory. | 47 |
| Clean Pointers | 48 | Clears pointer memory. | 48 |
| States | 49 | Switches state values. | 49 01 00 01 00 |
| TAB (if/cycles) | 50 | Marks code inside conditional/cycle. | 50 10 01 00 |
| End of cycle/statement | 51 | Ends a conditional or cycle. | 50 51 |
| If | 52 | Conditional statement. | 52 01 01 |
| While | 53 | Repeats code while condition true. | 53 02 00 34 01 10 |
| For | 54 | Loops for variable’s value count. | 54 01 00 |
| Do if | 55 | Runs at least once even if false. | 55 01 00 |
| Define | 56 | Creates a new definition. | 56 01 00 |
| TAB (define) | 57 | Adds code to definition. | 57 10 01 00 |
| Call definition | 58 | Calls a defined definition. | 58 01 00 |
| Lambda | 59 | Defines inline function-like definition. | 59 01 00 24 06 10 01 00 |
| Load TXT | 60 | Loads value from .txt file. | 60 01 00 24 01 05 |
| Save TXT in NumScript | 61 | Saves variable to .txt file (NumScript). | 61 01 00 24 01 05 |
| Save TXT in NumScript Ascii | 62 | Saves variable to .txt file (Ascii). | 62 01 00 24 01 05 |
| Import variables | 63 | Imports variables from JSON file. | 63 01 00 24 01 00 |
| Export variables | 64 | Exports variables to JSON file. | 64 01 00 24 01 00 |
| Import pointers | 65 | Imports pointers from file. | 65 01 00 24 01 05 |
| Export pointers | 66 | Exports pointers to file. | 66 01 00 24 01 05 |
| Import Definition | 67 | Imports definitions from JSON. | 67 01 00 24 01 00 |
| Export Definition | 68 | Exports definitions to JSON. | 68 01 00 24 01 00 |
| Load NS code | 69 | Loads NumScript code and executes. | 69 01 00 |
| Minimal | 70 | Keeps smallest token pair. | 10 01 00 01 01 70 |
| Maximal | 71 | Keeps largest token pair. | 10 01 00 01 01 71 |
| Average | 72 | Replaces tokens with average. | 10 01 00 01 04 72 |
| Sum | 73 | Replaces tokens with sum. | 10 01 03 01 02 73 |
| Length | 74 | Replaces with total token count. | 10 01 00 01 00 74 |
| Sort | 75 | Sorts token pairs. | 10 01 01 01 03 01 02 75 |
| Any | 76 | True if any token > 00. | 10 01 00 01 00 76 |
| All same | 77 | True if all tokens equal. | 10 01 01 01 01 77 |
| Random item | 78 | Picks random token. | 10 01 00 01 01 01 02 78 |
| Most common | 79 | Keeps most frequent token. | 10 01 00 01 00 01 01 79 |
| Shuffle | 80 | Randomizes token order. | 10 01 00 01 01 80 |
| Reverse | 81 | Reverses token order. | 10 01 02 01 03 81 |
| Poke variable memory name | 82 | Gets variable name by index. | 82 01 00 |
| Poke variable memory value | 83 | Gets variable value by index. | 83 01 00 |
| Insert to tokenized code | 84 | Inserts code to Tokenized Code. | 84 01 00 24 06 10 01 00 |
| Insert to higher tokenized code | 85 | Inserts code to higher tokenized. | 85 01 00 24 06 10 01 00 |
| Remove variable from memory | 86 | Deletes variable from memory. | 86 01 00 |
| Remove definition from memory | 87 | Deletes definition from memory. | 87 01 00 |
| Swap variable name/value | 88 | Swaps variable name and value. | 88 01 00 |
| Rename variable | 89 | Renames a variable. | 89 01 00 24 01 01 |
| Contains | 90 | Checks if item is in sequence. | 90 01 00 24 01 05 24 01 00 01 01 01 02 |
| Add tokens by index | 91 | Adds tokens to variable by index. | 91 01 00 24 01 00 24 01 01 |
| Remove token by index | 92 | Removes token by index. | 92 01 05 24 01 00 |
| Replace | 93 | Replaces token pair with another. | 93 01 00 24 01 00 24 01 01 24 01 00 01 00 |
| Replace by index | 94 | Replaces token at specific index. | 94 01 00 24 01 00 24 01 01 |
| Random randint | 95 | Sets variable to random int in range. | 95 01 00 24 01 00 24 01 05 |
| Substring | 96 | Extracts substring by start/end index. | 96 01 00 24 01 01 24 01 04 |
| &= | 97 | Sets variable to 01 if equal, else 00. | 97 01 00 24 01 00 |
| \|= | 98 | Sets variable to 00 if not equal, else 01. | 98 01 00 24 01 00 |
| Guide | 99 | Shows NumScript website URL. | 99 |

## NumScript Ascii 

| Code | Char | Code | Char | Code | Char | Code | Char | Code | Char |
|------|------|------|------|------|------|------|------|------|------|
| 00 | a | 01 | b | 02 | c | 03 | d | 04 | e |
| 05 | f | 06 | g | 07 | h | 08 | i | 09 | j |
| 10 | k | 11 | l | 12 | m | 13 | n | 14 | o |
| 15 | p | 16 | q | 17 | r | 18 | s | 19 | t |
| 20 | u | 21 | v | 22 | w | 23 | x | 24 | y |
| 25 | z | 26 | A | 27 | B | 28 | C | 29 | D |
| 30 | E | 31 | F | 32 | G | 33 | H | 34 | I |
| 35 | J | 36 | K | 37 | L | 38 | M | 39 | N |
| 40 | O | 41 | P | 42 | Q | 43 | R | 44 | S |
| 45 | T | 46 | U | 47 | V | 48 | W | 49 | X |
| 50 | Y | 51 | Z | 52 | 0 | 53 | 1 | 54 | 2 |
| 55 | 3 | 56 | 4 | 57 | 5 | 58 | 6 | 59 | 7 |
| 60 | 8 | 61 | 9 | 62 | ! | 63 | " | 64 | # |
| 65 | $ | 66 | % | 67 | & | 68 | ' | 69 | ( |
| 70 | ) | 71 | * | 72 | + | 73 | , | 74 | - |
| 75 | . | 76 | / | 77 | : | 78 | ; | 79 | < |
| 80 | = | 81 | > | 82 | ? | 83 | @ | 84 | [ |
| 85 | \\ | 86 | ] | 87 | ^ | 88 | _ | 89 | ` |
| 90 | { | 91 | &#124; | 92 | } | 93 | ~ | 94 | € |
| 95 | £ | 96 | ¥ | 97 | ¢ | 98 | § | 99 | ' ' |

## Code Examples

### Example of defining a variable and for cycle.

> NS Code split by new lines:

13 01 01 24 01 10
54 01 01
50 10 02 01
50 51

> NS code split by 25:

13 01 01 24 01 10 25 54 01 01 25 50 10 02 01 25 50 51

> Console output:

10
09
08
07
06
05
04
03
02
01

# NumScript: A numerical programming language

> NumScript is a lightweight, esoteric, interpreted scripting language designed for numerical programming and writing simple scripts. The language started as a joke back in middle of the 2024 and over time it grew into its current form featuring rich syntax.

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

> Run -> 00	Another way of running code inserted to console.	00

Number	01	num	Pointer towards a number.	01 00 -> 00 is a number
Variable (num)	02	var	Pointer towards variable by name.	02 00 -> Variable named 00
Variable (var)	03	var-var	Points to variable by value of variable	03 00 -> Variable named as value of variable 00
Index (num)	04	index-num	Replaces lexer block by numeric index.	01 00 01 01 04 00 -> 00
Index (var)	05	index-var	Replaces lexer block by variable value index.	01 00 01 01 05 00 -> token at variable 00's value
Rest is num	06	rest-num	Similar to number pointer but considers tge rest of line to be a number.	06 00 01 -> 00 01 is taken as a number
Rest is var	07	rest-var	Similar to variable pointer but considers the rest of line to be a variable.	07 00 01 -> 00 01 is taken as a variable
Pointer (num)	08	pointer-num	Calls all variables from a pointer where its name is a number.	08 00 -> Calls all variables from pointer 00
Pointer (var)	09	pointer-var	Calls all variables from a pointer where its name is a variable value.	09 00 -> Calls all variables from pointer named after value of variable 00
Print	10	print	Prints all lexer blocks.	10 01 00 -> prints 00
Print in NS Ascii	11	print-ascii	Prints all lexer blocks translated by NS Ascii.	11 01 00 -> prints A
Input	12	input	Adds user input to current lexer block.	10 12 -> prints tokens from input
Let	13	let	Defines a variable, first lexer block is its name, rest are combined to form its value.	13 01 00 24 01 10 -> Variable 00 with value 10
Define pointer	14	pointer-define	Defines a pointer, first lexer block is its name, rest are variable names.	14 01 00 24 01 05 24 01 07 -> Pointer with variables 05 and 07
Remove variable from pointer by name	15	pointer-remove-name	Removes specific variables from specific pointer.	15 01 00 24 01 05 -> Variable 05 is removed from pointer 00
Remove variable from pointer by index	16	pointer-remove-index	Removes specific variables from specific pointer by index.	15 01 00 24 01 05 -> Variable at index 05 is removed from pointer 00
Append to pointer	17	pointer-append	Adds variables from a pointer, first lexer block is pointers name, rest are variables.	17 01 00 24 01 00 -> Variable 00 is added
Merge Pointers	18	pointer-merge	Merges second pointer into the first one.	18 01 00 24 01 01 -> Pointer 01 is merged into pointer 00
Delete pointer	19	pointer-delete	Deletes specific pointer.	19 01 00 -> Pointer 00 is deleted.
Exit	20	exit	Ends the execution of a NumScript script.	20
Restart	21	restart	Restarts the console.	21
Comment	22	comment	Code comment, it can be used both before line and inside of a line.	22 10 01 00 -> Code is not executed
Split between variables	23	split-var	Used to determine split between variables in lexer block.	10 02 00 23 02 01 -> Prints variables 00 and 01
Split in lexer parts	24	split	Split between lexer blocks, for example used in defining variables.	13 01 00 24 01 00
Then	25	then	Allows writing multiple lines of code on one line.	10 01 00 25 10 01 01 -> 10 01 00, 10 01 01
Date	26	date	Calls current date as numerical value.	10 26 -> Prints 24 07 2025 for example
Time	27	time	Call current time as numerical value.	10 27 -> Prints 10 45 for example
Read down	28	read-down	Interpreter reads code from top to bottom.	28 -> Code is now being read from top to bottom
Read up	29	read-up	Interpreter reads code from bottom to top.	29 -> Code is now being read from bottom to top
+	30	+	Plus sign.	10 01 01 30 01 01 -> Prints 02
-	31	-	Minus sign.	10 01 01 31 01 01 -> Prints 00
*	32	*	Times sign.	10 01 01 31 01 01 -> Prints 01
/	33	/	Division sign.	10 01 01 31 01 01 -> Prints 01
>	34	>	Greater than sing.	10 01 00 34 01 01 -> Prints 00 since 00 is not smaller than 01
<	35	<	Smaller than sign.	10 01 01 35 01 01 -> Prints 00 since 01 is not bigger than 01
=	36	=	Equals sign.	10 01 01 36 01 01 -> Prints 01 since both sides are same
&	37	&	AND operator.	10 01 01 37 01 01 -> Prints 01 since 01 and 01 has the same value
|	38	|	OR operator.	10 01 01 38 01 01 -> Prints 01 since atleast one side is bigger than 00
~	39	~	NOT operator.	10 39 01 01 -> Does a bit flip -> -2 -> Prints 2
Jump	40	jump	Interpreter jumps to specific line.	40 01 00 -> Interpreter jumps to line number 00
Wait	41	wait	Script is frozen for a certain amount of time.	41 01 01 -> Script is frozen for 01 seconds
Clean Console	42	clean-console	Cleans console content.	42
Clean States	43	clean-states	Sets states to default values.	43
Clean Tokenized Code	44	clean-tokenized	Cleans Tokenized Code.	44
Clean Higher Priority Tokenized Code	45	clean-higher-tokenized	Cleans Higher Priority Tokenized Code.	45
Clean Variables	46	clean-variables	Cleans variable memory.	46
Clean Definitions	47	clean-definitions	Cleans definitions memory.	47
Clean Pointers	48	clean-pointers	Cleans pointer memory.	48
States	49	states	Switches states values.	49 01 00 01 00 -> Each 01/00 corresponds to specific setting, check rest of the guide for more info.
TAB (if/cycles)	50	tab	TAB used in conditional statement or cycle.	50 10 01 00 -> Everything after 50 is part of conditional statement or cycle
End of cycle/statement	51	end	End of a conditional statement or cycle.	50 51 -> End of conditional statement or cycle
If	52	if	Conditional statement, uses all lexer blocks as a condition, 00 = False, rest = True	52 01 01 -> True
While	53	while	Logically a combination of if and jump. Once at the end of the cycle, a jump is triggered back to the while statement.	53 02 00 34 01 10 -> Example of equation
For	54	for	For cycle combines all lexer blocks to get a name of variable (similar to let) which is its parameter. Amount of cycles is defined by this variable's value.	54 01 00 -> For variable 00
Do if	55	do-if	Same as If, but in this case the code is ran atleast once. This can be used in making manual cycles using Jump.	55 01 00 -> False, but it will be executed once.
Define	56	define	Used to define a definiton, all lexer blocks are combined to determined the name of this new definition.	56 01 00 -> Creates definition named 00
TAB (define)	57	add	TAB used to determine which code is to be added to definition after creating it.	57 10 01 00 -> 10 01 00 is added to the definiton
Call definition	58	call	Calls a definition, all lexer blocks are combined to determined the name of the called definition.	58 01 00 -> Calls definiton named 00
Lambda	59	lambda	Similar to define, first lexer block is definition named with rest being combined with its valued being the definition code.	59 01 00 24 06 10 01 00 -> Crates a definition named 00
Load TXT	60	load	Loads value from .txt file in NumScript token format and saves it to a variable. First lexer blocks defines variable into which the value will be saved and the rest define the filename.	27 01 00 24 01 05 -> Loads text from file named 05 and saves it in NumScript token format to variable 00
Save TXT in NumScript	61	save	Saves a variable value into .txt file in NumScript token format. Saves value into .txt file. First lexer blocks defines variable from which the value will be taken and the rest define the filename.	61 00 24 01 05 -> Saves value of variable 05 to file 00 in NumScript token format
Save TXT in NumScript Ascii	62	save-ascii	Saves a variable value into .txt file in NumScript Ascii format. Saves value into .txt file. First lexer blocks defines variable from which the value will be taken and the rest define the filename.	62 01 00 24 01 05 -> Saves value of variable 05 to file 00 in NumScript Ascii format
Import variables	63	import-var	Imports variables from a .json file. First lexer block defines the filename, rest define names of the variables that should be imported.	63 01 00 24 01 00 -> From file 00 a variable 00 is imported
Export variables	64	export-var	Exports variables into a .json file. First lexer block defines the filename, rest define names of the variables that should be exported.	64 01 00 24 01 00 -> Into file 00 a variable 00 is exported
Import pointers	65	import-pointer	Imports pointers from file.	65 01 00 24 01 05 -> Imports pointer 05 from file 00
Export pointers	66	export-pointer	Exports pointers to file.	66 01 00 24 01 05 -> Exports pointer 05 into file 00
Import Definition	67	import-def	Imports definitions from a .json file. First lexer block defines the filename, rest define names of the definitions that should be imported.	67 01 00 24 01 00 -> From file 00 a definition 00 is imported
Export Definition	68	export-def	Exports definitions into a .json file. First lexer block defines the filename, rest define names of the definitions that should be exported.	68 01 00 24 01 00 -> Into file 00 a definition 00 is exported
Load NS code	69	import-code	Loads NumScript code from a file and executes it. All lexer blocks are used to define the file name.	69 01 00 -> Code from file 00 is executed
Minimal	70	min	Takes values of token pairs from lexer block before the command and keeps the smallest token pair.	10 01 00 01 01 70 -> Prints 00
Maximal	71	max	Takes values of token pairs from lexer block before the command and keeps the biggest token pair.	10 01 00 01 01 71 -> Prints 01
Average	72	avr	Takes values of token pairs from lexer block before the command and replaces them with the average token value.	10 01 00 01 04 72 -> Prints 02
Sum	73	sum	Takes values of token pairs from lexer block before the command and replaces them with the sum of all of them.	10 01 03 01 02 73 -> Prints 05
Length	74	len	Replaces the tokens before the command with the total length of the token pairs in a specific lexer block where each token pair counts as +1 length.	10 01 00 01 00 74 -> Prints 02
Sort	75	sort	Sorts the token pairs before the command in a specific lexer block.	10 01 01 01 03 01 02 75 -> Prints 01 02 03
Any	76	any	If atleast one token pair before the command in a specific lexer block has bigger value than 00 all of the token pairs are replaced with 00, otherwise they are replaced with 00.	10 01 00 01 00 76 -> Prints 00
All same	77	all-same	Replaces all token pairs before the command in a specific lexer block with True/False (01/00) based on if all of the token pairs have same value.	10 01 01 01 01 77 -> Prints 01
Random item	78	random-item	Replaces all token pairs before the command in a specific lexer block with one of them.	10 01 00 01 01 01 02 78 -> Prints 02 for example
Most common	79	common	Replaces all token pairs before the command in a specific lexer block with the most common one.	10 01 00 01 00 01 01 79 -> Prints 00
Shuffle	80	shuffle	Randomizes the token order before the command in a specific lexer block.	10 01 00 01 01 80 -> Prints 01 00 for example
Reverse	81	reverse	Reverses the order of tokens before the command in a specific lexer block.	10 01 02 01 03 81 -> Prints 03 02
Poke variable memory name	82	poke-name	Grabs variable name by index from memory. All lexer blocks are combined to determine the index value.	82 01 00 -> Prints variable name under index 00
Poke variable memory value	83	poke-value	Grabs variable value by index from memory. All lexer blocks are combined to determine the index value.	83 01 00 -> Prints variable value under index 00
Insert to tokenized code	84	insert-tokenized	Inserts code to Tokenized Code. First lexer block defines the index and rest of lexer blocks are combined with its value being the inserted code.	84 01 00 24 06 10 01 00 -> Inserts 10 01 00 to Tokenized Code to index 00
Insert to higher tokenized code	85	insert-higher-tokenized	Inserts code to Higher Priority Tokenized Code. First lexer block defines the index and rest of lexer blocks are combined with its value being the inserted code.	85 01 00 24 06 10 01 00 -> Inserts 10 01 00 to Higher Priority Tokenized Code to index 00
Remove variable from memory	86	delete-var	Removes variables from memory. Each lexer block value defines a variable name that is to be removed from memory.	86 01 00 -> Removes variable 00 from memory
Remove definition from memory	87	delete-def	Removes definitions from memory. Each lexer block value defines a definition name that is to be removed from memory.	87 01 00 -> Removes definition 00 from memory
Swap variable name/value	88	swap-var	Swaps the name/value of a variable. All lexer blocks are combined to define a variable name.	88 01 00 -> Swaps the name/value of variable named 00
Rename variable	89	rename-var	Renames a variable with the value staying same. First lexer block defines the current name with the rest being combined to define the new name.	89 01 00 24 01 01 -> Variable 00 is renamed to 01
Contains	90	contains	First lexer block defines an item that NS will look for, second block defines a variable into which the result should be saved and the rest of the blocks are combined and NS checks if the item is located there.	90 01 00 24 01 05 24 01 00 01 01 01 02 -> 00 is in 00 01 02 so variable 05 is set to 01
Add tokens by index	91	add-token	Adds tokens into a variable by index. First lexer block defines variable name, second block defines index and the rest are combined to define the value that is to be added.	91 01 00 24 01 00 24 01 01 -> Adds 01 to index 00 of variable 00
Remove token by index	92	remove-token	Removes specific token by index. First lexer block defines variable name with the rest defining the index value.	92 01 05 24 01 00 -> Removes the token pair located at index 00 in variable 05
Replace	93	replace	Replaces token pair by another token pair in a specific token pair string. First lexer block defines variable where the result will be saved, second block defines original token, third block defines new token and the rest are combined to form a token string.	93 01 00 24 01 00 24 01 01 24 01 00 01 00 -> Variable 00 will have the value of 01 01
Replace by index	94	replace-idx	Replaces token at a specific index by a new one. First lexer block defines variable name, second block defines index and the rest form a new token.	94 01 00 24 01 00 24 01 01 -> Token pair at index 00 in variable 00 is replaced with 01
Random randint	95	random-randint	Sets the value of a variable as a random randint with a min/max. First lexer block defines variable name, second block defines min and third one defines maximum.	95 01 00 24 01 00 24 01 05 -> Variable 00 has the value of 03 for example
Substring	96	substring	Extracts part of string by index of start and end. First lexer block defines variable name where the result is to be saved, second block defines start and the rest are combined to define the end.	96 01 00 24 01 01 24 01 04 -> variable 00: 00 01 02 03 04 05, result 01 05
&=	97	&=	If variable value is same as token pair string, the variable is set to 01, else 00. First lexer block defines the variable name with the rest defining the token string.	97 01 00 24 01 00
|=	98	|=	If variable value is not same as token pair string, the variable is set to 00, else 01. First lexer block defines the variable name with the rest defining the token string.	98 01 00 24 01 00
Guide	99	guide	Shows the NumScript website URL.	99

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

# NumScript: A questionable programming language

## Overview

> NumScript, short for NumericalScript, is a lightweight, esoteric, interpreted scripting language designed for rapid numeric programming and writing simple scripts.

> Its syntax is built around two-digit numeric token pairs, each representing a command, operation, or keyword

> Current NumScript version is 1.4

## Key Features

> Token-Based Syntax: All instructions are built using numeric token pairs (e.g., 13, 01)..

> Zero-Error Policy: NumScript never crashes. Mistyped or incomplete code will default to safe (though potentially unintended) behavior.

> Real-Time Execution: The interpreter processes code one line at a time with immediate feedback.

> Simplicity: NumScript features a minimalistic syntax and a limited set of data types, resulting in a lightweight and fast programming experience.


## Development Team

> Head Developer: skirex - Developer of NumScript and NumScript Server

> Developer: benz.00 - Developer of NumScript and NumScript IDE

> Developer: excel_master - Consultant and support developer

## Core Mechanics

> NumScript is an interpreted language, meaning the interpreter reads and executes the code one line at a time.

> The code is first processed by a tokenizer, which verifies that its content is numeric and splits it into token pairs, for example 10-01-00.

> After tokenization, the tokens are analyzed by a parser to determine which function should be executed. This is defined by the first token pair.

> The first token pair is then removed, and the remaining tokens are passed to the lexer, which analyzes their content.

> The NumScript lexer outputs Lexer Blocks, which are groups of tokens representing final values. In code, these blocks are separated by the token 23.

> A good example of blocks is a variable definition: 13 01 00 23 01 01 01 00
    -> This expression contains two blocks: the first defines the variable name, and the second defines its value. The value of the first block is 00, and the value of the second block is 01 10.
    These blocks are then used as parameters in the functions being executed. When debugging is enabled, you can view each of these blocks in detail.

## Runtime Architecture

> Input: 10 01 00 -> Tokenizer: "10"-"01"-"00" -> Parser + lexer: Function "10" (Print) - Parameters ["00"] -> Console: 00

## Zero Error Policy

> NumScript is built to never throw errors during execution.
> Missing parameters are automatically replaced with default values.
> For example: 13 01 00 (missing value block) → Creates variable 00 with default value 00.

## NumScript Console
> NumScript has integrated console that can be used to execute code, it features multiple customizable settings:

1. Debug -> Enables printing of outputs from normally silent functions such as jump, wait, and others.

2. Splitter -> Splits token pairs in the console output (e.g., 0001 becomes 00 01).

3. Print tokens -> Displays both the Tokenized Code and Higher Priority Tokenized Code after each function execution.

4. Print memory -> Shows variable and definition memory states after each function execution.

## Code Examples

### Example of defining a variable and for cycle.

13 01 01 24 01 10

54 01 01

50 10 02 01

50 51

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

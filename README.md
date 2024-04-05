# AFLL-mini-project-UE22CS243A-
This project is a simple interpreter for the 'Swift' programming language. It uses the PLY (Python Lex-Yacc) library to implement the lexer and parser, which are the first two phases of a compiler or interpreter.
This project is a collection of lexers and parsers implemented using the PLY (Python Lex-Yacc) library in Python. Each pair of lexer and parser files is designed to interpret a specific construct of a programming language, such as 'if' statements, 'for' loops, 'for-in' loops, and 'while' loops.

The lexer files break down the input source code into a series of tokens. Tokens are the smallest meaningful units in a programming language, such as keywords, identifiers, operators, and punctuation symbols.

The parser files take the tokens produced by the lexer and check if they form a valid construct according to the rules of the programming language. They do this by matching the tokens against a set of grammar rules defined in the p_* functions. If the tokens match a rule, the parser builds a string that represents the structure of the matched rule. If the tokens don't match any rule, the p_error function is called to handle the syntax error.

Each parser can recognize and validate several types of statements in the language, including assignment statements, print statements, and arithmetic expressions. They also support logical operators in conditions and string literals in expressions.

The main loop at the end of each parser file reads lines of input from the user, parses each line, and prints whether the line is a valid statement in the language. If the parse result is None, it means there was a syntax error.

# Steps to run the program
1.First run the .lex file.
2.Next run the .yacc file of the corresponding programming construct.
3.This will start a loop that reads lines of input from the user, parses each line, and prints whether the line is a valid statement in the language.

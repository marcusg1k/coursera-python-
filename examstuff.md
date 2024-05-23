Study guide functions: 

Terms to remember: 
return value: the value or variable returned as the end result of a function

parameter(argument): a value passed into a function for use within the function

refactoring code: a process to restructure code without changing functionality


Knowledge purposes:
The purpose of the def() keyword is to define a new function
Best practices for writing code that is readable and reusable: 
Create a reusable function: replace duplicate code with one reusable function ot make the code easier to read and repurpose
Refactor code: Update code so that it is self-documenting and the intent of the code is clear.
Add comments: Adding comments is part of creating self-documenting code. Using comments, allows you to leave notes to yourself and/or other programmers to make the purpose of the code clear. 


Review: Comparing things

Introduction
This follow-along reading is organized to match the content in the video that follows. It contains the same code shown in the next video. These code blocks will provide you with the opportunity to see how the code is written, allow you to practice running it, and can be used as a reference to refer back to. 

Logical operators: AND, OR, NOT
To evaluate as true, the operator AND would need both expressions to be true at the same time
To evalute as true, the operator OR would need only 1 of the conditions to be true to return as true
The NOT operator inverts the value of the expression thats in front of it
if expression is true it becomes false, if it is false it becomes true

"==" (equality)
"!=" (not equal to) 
">" (greater than)
"<" (less than)
">=" (greater than or equal to)
"<=" (less than or equal to) 

a == a AND a != b (true if both sides are true, otherwise false)
a > b or a <= c (true if either side is True. False is both sides are false)
NOT a == b (true if the statement is false, false if the statement is true) 

the body of the block will only execute when the condition evaluates to true; otherwise it's skipped

Comparison expressions return a Boolean result (True or False). 
x == y        If x is equal to y, return True. Else, return False.
x != y         If x is not equal to y, return True. Else, return False.
x < y          If x is less than y, return True. Else, return False.
x <= y        If x is less than or equal to y, return True. Else, return False.
x > y          If x is greater than y, return True. Else, return False.
x >= y        If x is greater or equal to y, return True. Else, return False.
Comparison expressions with strings also return a Boolean result (True or False).
"x" == "y"  If the words are the same, return True. Else, return False.
"x" != "y"   If the words are not the same, return True. Else, return False.
When used with strings, the following comparison expressions will alphabetize the strings.
"x" < "y"   	If string "x"  has a smaller Unicode value than string "y", return True.  Else, return False.
"x" <= "y" 	If the Unicode value for string "x" is smaller than or equal to the Unicode value of string "y", return True. Else, return False.
"x" > "y"    	If string "x" has a larger Unicode value than string "y", return True. Else, return False.
"x" >= "y"  	If the Unicode value for string "x" is greater than or equal to the Unicode value of string "y", return True. Else, return False.
syntax for an if-elif-else block
if condition1: 
    action1
elif condition2: 
    action2
else:
    action3

Glossary terms to remember(course1, module 2) 
Built in functions: Functions that exist with Python and can be called directly
Comments: Notes to yourself and/or other programmers to make the purpose of the code clear
Data types: Classes of data(example: string, int, float, boolean) which include properties and behaviors of instances of the data type (variables)
Explicit Conversion: This occurs when code is written to manually convert one data type to another using a data type conversion function
Expression: A combination of numbers, symbols, or other values that produce a result when evaluated
Implicit conversion: This occurs when the python interpreter automatically converts one data type to another
Logical Operators: Operators used to combine or manipulate boolean values (True or False) to create complex conditions for decision making
Parameter(argument): A value passed into a function for use within the function, controlling the behavior of the CSV reader and writer
Refactoring: When a code is updated to be more self-documenting and clarify the intent
Return value: This is the value or variable returned as the end result of a function

while loops: instruct computer to continuously execute your code based on the value of a condition
(remember to initialize variables and check that loops wont run forever) 
while "specified condition" is True:
    body of loop

infinite loop: missing a method for exiting the loop, causing loop to run forever

break: a break statement in python provides a way to exit out of a loop before the loop's condition is false. Once a break statement is encountered, the program's control flow jumps out of the loop and continues executing the code after the loop

pass: A pass statement in python is a placeholder statement which is used when the syntax requires a statement, but you don't want to execute any code or command

math concepts for practice quiz: 
prime numbers: integers that have only two factors
prime factors: prime numbers that are factors of an integer
divisor: a number denominator that is used to divide another number
sum of all divisors of a number: the result of adding all of the divisors of a number together
multiplication table: an integer multiplied by a series of numbers and their results formatted as a table or a list

dealing with ranges: In python and a lot of other programming languages, a range of numbers will start with the value 0 by default
The list of numbers generated will be one less then the given value.

Use FOR loops when there's a sequence of elements that you want to iterate
Use WHILE loops when you want to repeat an action until a condition changes

for loops
for x in range(5): 
    print(x) #outputs 0, 1, 2, 3, 4
for loop recap: enable you to iterate over a sequence of values, such as numbers, names, or lines in a file
You can even iterate over a list of strings.

What are strings?
Strings represent a sequence of characters and are often used to display output to the user. 
You can recognize a string because it is usually surronded by single or double quotes. "String" 'string' 

for vs while loops
while loops are used when a segment of code needs to execute repeatedly while a condition is true
for loops iterate over a sequence of elements, executing the body of the loop for each element in the sequence

recursion

range() function can take up to three parameters: range(start, stop, step)
start: first item in range()
stop: second item in range()
step: third item in the range() 

break: A way to exit out of a loop before the loop's condition is false
control statements: programming constructs that direct the flow of execution of a program by allowing you to make decisions, repeat actions, or choose between different code paths based on specfic conditions
For loop: this executes a block of code for a specified number of iterations or over a collection of items
infinite loop: a sequence that is missing a method for eiting the loop, causing the loop to run forever
iterators: variables that allow you to loop through a collection one item at a time
loop: a sequence that makes the computer do repetitive tasks
programming: the process of writing a program to behave in different ways
pass: a placeholder statement which is used when the syntax requires a statement, but you dont want to execute any code or command
recursion: the repeated application of the same procedure to a smaller problem
while loop: this is used when a segment of code needs to execute repeatedly while a condition is true 

Module 3 stuff: 
variables: know how ot properly initialize or increment a variable, you will also need to recognize a coding error due to the failure to properly initlialize a variable

infinite loops: know how to recognize infinite loops and use common solutions to prevent them, check loop conditions, ranges, iterators, control statements

Iterators: know the various options available for iterating a variable (using assignment operators) using the third range() function

control statements: know how and when to use the break and continue control statements to prevent infinite loops

common functions: 
range() function parameters - know roles of the three possible range(x, y, z)
x = start of range (included)
y = end of range (excluded index)
z = incremental value

print() Function default behavior

String operations and methods
.format() = string method that can be used to concatenate and format strings

{:2f} = within the .format() method, limits a floating point variable to 2 decimal places. The number of decimal places can be customized. 

len(string) = string operation that returns the length of the string

string[x] = string operation that accesses the character at index [x] of the string, where indexing starts zero

string [x:y] = string operation that accessses a substring starting at index [x] and ending at index [y-1] 

string.replace(old, new) = string method that returns a new string where all occurrences of an old substring have been replaced by a new substring

string.lower() = string method that returns a copy of the string with all lowercase characters

List = sequences of elements of any type and are mutable
tuples = sequences of elements of any type, that are immutable

len(sequence) - returns the length of the sequence
for element in sequence - iterates over each element in the sequence
if element in sequence - checks whether the element is part of the sequence
sequence[x] - accesses the element at index [x] of the sequence, starting at zero
sequence[x:y] - accesses a slice starting at index [x], ending at index [y-1]. If [x] is omitted, the index will start at 0 by default. If [y] is omitted, the len(sequence) will set the ending index position by default
for index, element in enumerate(sequence) - iterates over both the indices and the elements in the sequence at the same time

list[index] = x - replaces the element at index [n] with x
list.append(x) - Appends x to the end of the list
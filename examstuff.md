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


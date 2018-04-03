# EasyDoc
Some code to extract documentation from a .py file and write it to .txt

Gives one .txt file with the documentation of functions and one .txt file with the documentation
of classes and functions of the classes.

Assumes all indents are 4 spaces. 

The .txt files are written in the same directory as the python file

See wiki for example output (the .txt output has been copy pasted to wiki page)

## Notes:
Assumes that it is going to be posted to a github wiki and does some formating
Returns a list of functions and the doc in a .txt file. 

## There are a few limitiations:
Only functions that are not indented are found. 
Only reads doc witch start and end with ''' (does not read """)
For classes it only looks for functions that are indented once. 


## Example:
A file called 'example.py' containing the following two functions and 1 class. 

Use the docsToText function in easyDoc

´>>> filename = 'example.py'´

´>>> docsToText(filename)´

Returns: 2 .txt files

exampleFuncDoc.txt

exampleClassDoc.txt


**See the wiki for copy pasted output**






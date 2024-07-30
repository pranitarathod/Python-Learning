# How do you write comments in python? and why comments are important?

'''
>>comments can be uesd to make the code more readable and it is used to prevent execution when testing code.
>>Comments can be placed at the end of a line, and python will ignore the rest of the line.
>> #- (single uesd to comment)
>>Control + / (used for multiple statements)
>>multiple string- (uesd for triple quotes) 
'''

# what do you mean by python literals?
'''
>>literals are a notation for representing a fixed value in source code. they can also be defined as raw value or data given in 
variable or constant.
>>python literals are the values that are written directly in the code.
'''

#different ways to assign value to variable.
'''
1. way
a = 34
b = 45
c = 23

2. way
a=b=c= 320

3. way
a=23; b=34; 56=23

4. way

c = a+b+c+d
'''

#escape character
'''
>>An escape character is a backslash\followed by the character you want to insert.
1. \ --- It can escape quotes.

eg. s10 = 'hey, what\'s up'  #we use \
    print(s10,type(s10))
    
o/p - hey, what's up <class 'str'>

2. \n --- to insert enter in a string or to print text on new line.

eg. string = "Data science \nis an interdisciplinary field \nthat uses scientific methods"
    print(string)

o/p - Data science 
      is an interdisciplinary field 
      that uses scientific methods

3. \t - to insert tab in the string.

eg. str1 = 'helloworld'
    print(str1)

o/p - helloworld  

'''

#which are the different ways to perform string formatting? explain with example.
'''
There are two ways of string formatting.
1) F String Formatting

Syntax of F string: Print (f 'Function {a}, {b} is {Operation}')

2) .Format string Formatting

Syntax of Format string: Print ('function {}, {} is {}.' format (a, b, operation)

Example of F string and format string is as follows:

# f string example

a = 20
b = 30
c = 50
add = a + b + c
print(f'addition of {a}, {b}, and {c} is:',{add})

o/p---addition of 20, 30, and 50 is: {100}

# .format string example

a = 32
b = 54
c = 43
add = a + b + c
print('addition of {}, {} , and {}, is {}:'.format(a, b, c, add))

o/p---addition of 32, 54 , and 43, is 129:

'''

#what is index?
'''
An index is a position of an individual character or element in a list, tuple, or string. 
The index value always starts at zero and ends at one less than the number of items.

'''

#string slicing--

'''' 
Slicing is the extraction of a part of a string, list, or tuple. 
It enables users to access the specific range of elements by mentioning their indices.

syntax 
string[start_inedx:end_index] # start index ---> included & end_index not included

start_index --- included
end_index --- not included
'''
##String Slicing with negative indexing 
'''
string = "Data"

# D   a  t  a
# 0   1  2  3
# -4 -3 -2  -1

# # at
# slicing syntax 
# var[start_index:end_index]

print(string[-3:])
'''

##Step Size
'''
Syntax 

var[start_index:end_index:step_size]

start_index -- included by default 0
end _index --- not include by deafult last index
step_size --- how many number of jump for slicinig (char to skip) by default 1
'''

#Slice() function
'''
The slice() method extracts a section of data and returns it as new data, without modifying it. 
This means users can take a specific range of elements without changing it.
'''

#string concatenation
'''
To concatenate, or combine, two strings you can use the + operator.

eg. 

'''

'''Casefold
return casefolded copy of string.casefolded string may be caseless matching.it is similar to lowercase.  

'''

'''
list & tuple
[]             |    ()
mutuable       | immutable
slower         | Faster
more time      | less time to execute
more memory    | less memory 
more methods/fun | less methods
ordered        | Orderes
allow duplicate| Allow duplicate
separetd by ,  | separated by comma ,
contain diff data | contain diff data
index & slicing | index & slicing
'''
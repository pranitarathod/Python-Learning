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
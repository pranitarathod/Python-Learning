#Write a program to find the length of the string "machne learning" with and without using len function.

#without using len function
string = "Machine Learning"
count = 0
for i in string:
    count = count + 1
print("index is:", count)

#with using len function
string = "Machine Learning"
print(len(string))
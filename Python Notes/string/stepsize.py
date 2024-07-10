#Step Size
'''
Syntax 

var[start_index:end_index:step_size]

start_index -- included by default 0
end _index --- not include by deafult last index
step_size --- how many number of jump for slicinig (char to skip) by default 1
'''

str1 = "Data science is an interdisciplinary field that uses scientific methods"
print(len(str1))
print(str1[::])
print(str1[0:70:2])
print(str1[0:70:3])
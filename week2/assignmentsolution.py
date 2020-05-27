import re

""" 
filename = open('regex_sum_594718.txt')         #   FOR SAMPLE USE >>filename = open('regex_sum_42.txt')
filename = filename.read()                      #   THIS VARIABLE HOLDS CONTENT OF FILE
lst = re.findall('[0-9]+',filename)             #   REGEX STRING THAT LOOK FOR INTEGERS AND RETURNS STRINGS IN LIST
count = 0                                       #   VARIABLE STORING SUM OF NUMBERS IN LIST
for number in lst:
    count = count + int(number)                 #   SUMMING NUMBERS
print(count) 
"""



#Optional: Just for Fun
#most compact code using list comprehension

print( sum( [ int(number) for number in re.findall('[0-9]+',open('regex_sum_594718.txt').read()) ] ) )


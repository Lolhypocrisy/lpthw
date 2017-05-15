#imports argv from module sys
from sys import argv
#sets up what argv needs for inputs
script = argv
#opens text file and puts its contents into txt variable
filename = input("Enter file name:")
txt = open(filename)
#prints filename
print(f"Here's your file {filename}:")
#prints contents of file
print(txt.read())
txt.close()

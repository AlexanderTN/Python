from sys import argv

script, filename = argv

txt = open(filename,'r')
print(txt.read())   
# Always remember to close the file after finish
txt.close()
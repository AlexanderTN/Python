# -*- coding: utf-8 -*-

from sys import argv

script, file_name = argv

#Warning the user
print "We're going to erase %r." % file_name
print "If you don't want that, hit CTRL+C (^C)."
print "If you do want that, hit RETURN (ENTER)."
raw_input('?')
print "Opening the file"
txt_file = open(file_name, "w")

print "Truncating the file. Goodbye!"
txt_file.truncate()

print "Now I'm going to ask you for 3 lines"

#raw_input('File %s was truncated. Does it hurt you? >')
#print "Now we gonna write into that file"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: " )

txt_file.write(line1 + "\n")
txt_file.write(line2)

print "And finally, we close it."
txt_file.close()
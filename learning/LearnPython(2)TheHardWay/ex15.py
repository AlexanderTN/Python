# -*- coding: utf-8 -*-

from sys import argv

script, file_name = argv
txt = open(file_name)
print txt.read()
#remember to close the file after open it
txt.close()
txt_again = raw_input('Input the file name again\n > ')
txt_file_again = open(txt_again)

print txt_file_again.read()
txt_file_again.close()
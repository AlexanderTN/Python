# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv
'''
print "copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytess long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
'''
#just try to do it in one line
open(to_file, 'w').write(open(from_file).read())
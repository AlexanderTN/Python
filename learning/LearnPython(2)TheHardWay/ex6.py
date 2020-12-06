# -*- coding: utf-8 -*-
# assign X to a string as below, %d is replaced with 10 first
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# replace %s and %s with binary and do_not
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

#assign a boolean value
hilarious = False
#This line is strange at the first look
joke_evaluation = "Isn't that joke so funny y?! %r"

#This line take the joke_evaluatio and replace %r with hilarious
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
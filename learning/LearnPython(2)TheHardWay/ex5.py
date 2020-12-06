# -*- coding: utf-8 -*-
# More Variables and Printing
name = 'Tam H. Nguyen'
age = 26 # not a lie
height = 1.75 # meters
height_in_inch = height * 100 / 2.54
weight = 61 # kg
weight_in_pounds = weight * 2.2
eyes = 'Black'
teeth = 'White'
hair = 'Brown'
fuck = [2, 3]
for f in fuck:
   print "fuck %r" % f
print "Let's talk about %s" % name
print "He's %s meters (%s inches) tall" % (height, height_in_inch)
print "He's %d kilograms (%r pounds) heavy" % (weight, weight_in_pounds)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depening on the coffee" % teeth

# this line is a tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
# -*- coding: utf8 -*-
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %s heavy." % (
    age, height, weight
)


# Another way to use raw_input(And I think it's the more popular way
hello = raw_input('Hello, How are you')
print "You are %s" % hello



# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
)
xxx = [5, 6, 7, 8]
print "%r" % xxx
#Well, the result is strange, in the last line, there are both '' and ""
#I have the answer, if the string contain "'" in it so that the out put will be ""
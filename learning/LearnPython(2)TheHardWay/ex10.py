# -*- coding: utf-8 -*-
'''
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """ xxx
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
'''
import time
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
    time.sleep(0.1)
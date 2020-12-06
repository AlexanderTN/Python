tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catip\n\b\t* Grass
{}
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat.format("\t\b\b*** Nothing special, really nigga\b"))

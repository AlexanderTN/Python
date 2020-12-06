# ex18.py Names, Variables, Code, Functions
# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg3}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just take one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no argument
def print_none2():
    print("I got nothing")

print_two("Zed", "Shaw", "xxx")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none2()
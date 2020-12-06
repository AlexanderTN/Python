#ex33.py While Loop

numbersx = []

def AddNumber(number, step, numbers):
    i = 0     
    while i < number:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += step
        print("Numbers now: ", numbers)
        print(f"X At the bottom i is {i}")

#ok now I rewrite it using for-loop and range
def AddNumberFor(number, step, numbers):
    for i in range(0, number, step):
        print(f"At the top i is {i}")
        numbers.append(i)    
        i += step
        print("Numbers now: ", numbers)
        print(f"Y At the bottom i is {i + step}")   

AddNumber(6, 2, numbersx)
AddNumberFor(6, 2, numbersx)
print("The numbers: ")

for num in numbersx:
    print(num)
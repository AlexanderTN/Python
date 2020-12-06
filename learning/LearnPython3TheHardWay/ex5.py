name = "Tam H. Nguyen"
age = 32 # Not a lie, not very young
height = 175 #cm, in inches = 175/2.54 = 68.897637795275591
height_in_inches = height / 2.54
weight = 65 #kg, in pound: lb = 65 * 2.20462 = 143.3 lb
weight_in_pound = weight * 2.20462
eyes = "Black"
teeth = "Yellow"
hair = "Black"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, {weight} I get {total}.")




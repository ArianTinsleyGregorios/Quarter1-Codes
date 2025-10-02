fullname = inout("Enter your full name (First, Middle, Last): ")
first, middle, last = [name.strip() for name in fullname.split(',')]
first = first.capitalize()
last = last.capitalize()
middle = middle[0].upper() + '.'
print(f"Formatted Name: {last}, {first} {middle}")
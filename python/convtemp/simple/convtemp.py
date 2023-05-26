from sys import argv

if len(argv) != 3:
    print("Incorrect number of arguments")
    exit(1)

if argv[1].lower() not in ('f','c','farhenheit','celsius'):
    print("First argument has to be one of 'f' 'c' 'fahrenheit' or 'celsius'")
    exit(2)

try:
    in_temp = float(argv[2])
except:
    print("Second argument needs to be a number")
    exit(3)

# Using argv[2] for output so that it will print out the same number as inputed
# Ex: 2 instead of 2.0
if argv[1].lower() in ('f', 'farhenheit'):
    ctemp = (in_temp - 32) * 5.0/9
    print(f"{argv[2]}f is {ctemp:.1f}c")

if argv[1].lower() in ('c', 'celsius'):
    ftemp = (in_temp * 9.0/5) + 32
    print(f"{argv[2]}c is {ftemp:.1f}f")

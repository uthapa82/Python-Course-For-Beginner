filename = 'learning_python.txt'

print("Reading entire file.")
with open(filename) as file:
    contents = file.read()
    print(contents)

print("looping over fileobject.")
with open(filename) as file:
    for line in file:
        print(line.rstrip())

print("Storing line in a list.")
with open(filename) as file:
    lines = file.read()

for line in lines:
    print(line.rstrip())
file = open("README.md", "r")
string = file.read()
names = string.split(" ")
for name in names:
    print(name)

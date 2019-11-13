file = open("readme.md")
read_file = file.read
names = read_file.split(" ")
for name in names:
    print(name)
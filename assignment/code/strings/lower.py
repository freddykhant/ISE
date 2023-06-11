def to_lower(string):
    return string.lower()

def IOto_lower():
    string = input("Enter a string: ")
    print(to_lower(string))

def fileIOto_lower(filename, line):
    with open(filename, "r+") as file:
        lines = file.readlines()
        string = lines[line]
        file.write("\n" + to_lower(string))
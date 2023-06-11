def to_upper(string):
    return string.upper()

def IOto_upper():
    string = input("Enter a string: ")
    print(to_upper(string))

def fileIOto_upper(filename, line):
    with open(filename, "r+") as file:
        lines = file.readlines()
        string = lines[line]
        file.write("\n" + to_upper(string))
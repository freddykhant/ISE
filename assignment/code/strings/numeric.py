def is_numeric(string):
    for character in string:
        if character.isdigit():
            return True
    return False

def IOis_numeric():
    string = input("Enter a string: ")
    print(is_numeric(string))

def fileIOis_numeric(filename, line):
    with open(filename, "r+") as file:
        lines = file.readlines()
        string = lines[line]
        file.write("\n" + str(is_numeric(string)))
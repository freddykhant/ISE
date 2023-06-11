def is_number(string):
    if string.isnumeric():
        return True
    else:
        return False

def IOis_number():
    string = input("Enter a string: ")
    print(is_number(string))

def fileIOis_number(filename, line):
    with open(filename, "r+") as file:
        lines = file.readlines()
        string = lines[line]
        file.write("\n" + str(is_number(string)))
import upper, numeric

def convert_upper(string):
    if numeric.is_numeric(string):
        result = upper.to_upper(''.join([c for c in string if not c.isdigit()]))
        return result
    else:
        return upper.to_upper(string)

def IOconvert_upper():
    string = input("Enter a string: ")
    print(upper.convert_upper(string))

def fileIOconvert_upper(filename, line):
    with open(filename, "r+") as file:
        lines = file.readlines()
        string = lines[line]
        file.write("\n" + upper.convert_upper(string))
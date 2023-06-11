import lower, numeric

def convert_lower(string):
    if numeric.is_numeric(string):
        result = lower.to_lower(''.join([c for c in string if not c.isdigit()]))
        return result
    else:
        return lower.to_lower(string)

def IOconvert_lower():
    string = input("Enter a string: ")
    print(lower.convert_lower(string))

def fileIOconvert_lower(filename, line):
    with open(filename, "r+") as file:
        lines = file.readlines()
        string = lines[line]
        file.write("\n" + lower.convert_lower(string))
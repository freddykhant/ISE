def seconds_to_mins(second):
    if second > 0:
        min = second/60
        return min
    else:
        print("Invalid time")

def IOseconds_to_mins():
    print("Enter time in seconds:")
    second = int(input())
    min = seconds_to_mins(second)
    print(min, "mins")

def file_seconds_to_mins(filename, line):
    with open(filename, "r+") as file:
        lines = file.readlines()
        second = int(lines[line])
        min = seconds_to_mins(second)
        file.write("\n" + str(min))
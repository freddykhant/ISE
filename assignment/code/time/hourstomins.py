def hours_to_mins(hour):
    if hour > 0:
        min = hour*60
        return min
    else:
        print("Invalid time")

def IOhours_to_mins():
    print("Enter time in hours:")
    hour = int(input())
    min = hours_to_mins(hour)
    print(min, "mins")

def file_hours_to_mins(filename, line):
    with open(filename, "r+") as file:
        lines = file.readlines()
        hour = int(lines[line])
        min = hours_to_mins(hour)
        file.write("\n" + str(min))
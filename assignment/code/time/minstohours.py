def mins_to_hours(min):
    if min > 0:
        hour = min/60
        return hour
    else:
        print("Invalid time")

def IOmins_to_hours():
    print("Enter time in mins:")
    min = int(input())
    hour = mins_to_hours(min)
    print(hour, "hrs")

def file_mins_to_hours(filename, line):
    with open(filename, "r+") as file:
        lines = file.readlines()
        min = int(lines[line])
        hour = mins_to_hours(min)
        file.write("\n" + str(hour))
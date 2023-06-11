def mins_to_seconds(min):
    if min > 0:
        second = min*60
        return second
    else:
        print("Invalid time")

def IOmins_to_seconds():
    print("Enter time in mins:")
    min = int(input())
    second = mins_to_seconds(min)
    print(second, "s")

def file_mins_to_seconds(filename, line):
    with open(filename, "r+") as file:
        lines = file.readlines()
        min = int(lines[line])
        second = mins_to_seconds(min)
        file.write("\n" + str(second))
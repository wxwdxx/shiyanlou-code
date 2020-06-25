import sys

def Hours(TimeM):
    try:
        Total_M = int(TimeM)
        if Total_M < 0:
            raise ValueError
        else:
            hour = int(Total_M / 60)
            minute = Total_M % 60
            return hour , minute
    except ValueError:
        print("please input a positive, int number")
        exit()

if __name__ == '__main__':
    hour, minute = Hours(sys.argv[1])
    print("{} H, {} M".format(hour,minute))

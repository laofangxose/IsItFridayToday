import datetime

if __name__ == '__main__':
    if datetime.datetime.now().weekday() == 4:
        print("Yes")
    else:
        print("No")

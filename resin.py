import cmd
import math
import datetime


def getInput():
    num = int(input("Enter your amount of resin: "))
    if num >= 160:
        print("Go and use your resin, ya dolt")
        exit()
    return num


def calcHours(mins):
    total = mins / 60
    hrs = math.floor(total)
    remainder = total - hrs
    fraction = remainder.as_integer_ratio()
    mins = math.ceil(60 * fraction[0] / fraction[1])
    return [hrs,mins]


def calcFinishTime(hrs, mins):
    now = datetime.datetime.now().time()
    finishHr = now.hour + hrs
    finishMin = now.minute + mins

    cleaned = clean(finishHr, finishMin)
    return cleaned


def clean(hr, min):
    modifier = "AM"
    swaps = 0
    while min >= 60:
        min -= 60
        hr += 1
    while hr > 12:
        hr -= 12
        modifier = swap(modifier)
        swaps += 1
    if swaps >= 2:
        modifier += " Tomorrow."
    else:
        modifier += "."

    return f"{hr}:{str(min).zfill(2)} {modifier}"


def swap(modifier):
    if modifier == "AM":
        modifier = "PM"
    else:
        modifier = "AM"
    return modifier


if __name__ == '__main__':
    input = getInput()

    resinToGain = 160 - input
    totalMins = resinToGain * 8

    time = calcHours(totalMins)
    hrs = time[0]
    mins = time[1]

    finishTime = calcFinishTime(hrs, mins)

    print('\n')
    print(f'Your resin will take {hrs} hours and {mins} minutes to fully regenerate.')
    print('\n')
    print(f'It will finish at {finishTime}')
    print('\n')
    
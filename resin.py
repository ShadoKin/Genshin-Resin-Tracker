import cmd
import math
import datetime


def getInput():
    num = int(input("Enter your amount of resin: "))
    if num >= 160:
        print("Go and use your resin, ya dolt")
        exit()
    elif num < 0:
        print("that is not possible, try again")
        getInput()
    return num

def getTarget(input_resin):
    num = int(input("Enter how much resin you want regenerated: "))
    if num < input_resin:
        print("You can't regenerate less than you have, try again")
        getTarget(input_resin)
    else:
        return num
    return -1


def calcTotalHours(mins):
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
    input_resin = getInput()
    target = getTarget(input_resin)

    resinToGain = 160 - input_resin
    totalMins = resinToGain * 8

    total_time = calcTotalHours(totalMins)
    total_hrs = total_time[0]
    total_mins = total_time[1]

    finishTime = calcFinishTime(total_hrs, total_mins)

    targetResinToGain = target - input_resin
    targetMins = targetResinToGain * 8

    target_time = calcTotalHours(targetMins)
    target_hrs = target_time[0]
    target_mins = target_time[1]

    targetTime = calcFinishTime(target_hrs, target_mins)

    print('\n')
    print(f'Your resin will take {total_hrs} hours and {total_mins} minutes to fully regenerate.')
    print(f'It will finish at {finishTime}')
    print('\n')
    print(f'Your resin will take {target_hrs} hours and {target_mins} minutes to regenerate.')
    print(f'It will finish at {targetTime}')
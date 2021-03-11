HOURS_PER_WEEK = 40
EXTRA_MULTIPLIER = 1.5

def computepay(hours, rate):
    hours = int(hours)
    rate = float(rate)
    pay = 0

    if hours <= HOURS_PER_WEEK:
        pay = hours * rate
    else:
        pay = HOURS_PER_WEEK * rate
        extra = (hours - HOURS_PER_WEEK) * rate * EXTRA_MULTIPLIER
        pay = pay + extra

    return pay

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = computepay(hours, rate)
print("Pay", pay)
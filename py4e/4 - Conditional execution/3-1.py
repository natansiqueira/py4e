HOURS_PER_WEEK = 40
EXTRA_MULTIPLIER = 1.5

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

hours = int(hours)
rate = float(rate)
pay = 0

if hours <= HOURS_PER_WEEK:
    pay = hours * rate
else:
    pay = HOURS_PER_WEEK * rate
    extra = (hours - HOURS_PER_WEEK) * rate * EXTRA_MULTIPLIER
    pay = pay + extra

print(pay)
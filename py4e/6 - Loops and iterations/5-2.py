largest = None
smallest = None

while True:
    number = input("Enter a number: ")

    if number == "done":
        break

    try:
        number = int(number)
    except:
        print("Invalid input")
        continue

    if smallest is None:
        smallest = number

    if largest is None:
        largest = number

    if number < smallest:
        smallest = number

    if number > largest:
        largest = number

print("Maximum is", largest)
print("Minimum is", smallest)
"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

file_name = input("Enter file name: ")
try:
    file_handle = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit()

messages_by_hour = {}

for line in file_handle:
    line = line.rstrip()
    if line.startswith("From "):
        time = line.split()[5]
        hour = time.split(":")[0]
        messages_by_hour[hour] = messages_by_hour.get(hour, 0) + 1

for k, v in sorted(messages_by_hour.items()):
    print(k, v)

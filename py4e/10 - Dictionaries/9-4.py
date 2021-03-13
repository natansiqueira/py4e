"""
Write a program to read through the mbox-short.txt and figure out who has sent
the greatest number of mail messages. The program looks for 'From ' lines and
takes the second word of those lines as the person who sent the mail. The program creates a
Python dictionary that maps the sender's mail address to a count of the number of times they
appear in the file. After the dictionary is produced, the program reads through the dictionary using a
maximum loop to find the most prolific committer.
"""
file_name = input("Enter file name: ")
try:
    file_handle = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit()

senders = {}

for line in file_handle:
    line = line.rstrip()
    if line.startswith("From: "):
        sender = line.split()[1]
        senders[sender] = senders.get(sender, 0) + 1

sends = None
sender_with_most_sends = None
for sender, count in senders.items():
    if sends is None or count > sends:
        sends = count
        sender_with_most_sends = sender

print(sender_with_most_sends, sends)
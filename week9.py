##week 9
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith("From:"):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email,0) + 1

big = None
small = None
for me,us in counts.items():
    if big == None : big = us
    if big <= us : 
        big = us
        small = me
print small, big
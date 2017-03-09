##week 10

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        email = words[5]
        hours = email [0:2]
        counts[hours] = counts.get(hours,0) + 1

c = list()

for me,us in counts.items():
    c.append ( (me,us) )
print c
c.sort()

for me, us in c:
    print me, us

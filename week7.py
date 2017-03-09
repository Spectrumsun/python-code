#week7
# Use words.txt as the file name
ff = raw_input ("enter file name")
x = open(ff)
inp = x.read()
print inp.upper().rstrip()



###
total = 0
count = 0
file = raw_input("Enter file name")
fn = open(file)
for line in fn:
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.rstrip()
        a = line.find(":")
        b = line.find(" ")
        x = line[a+2:b+26]
        t = float(x)
        total = total + t
        count = count + 1
print "Average spam confidence:", total / count 

#week 3
hor = raw_input("Enter Hours")
hours = float(hor)
rat = raw_input ("Enter Rate")
rate = float (rat)
pay = hours * rate
if hours <= 40 :
    pay = rate * hours
if pay > 40 :
    pay = rate * 40 + (rate * 1.5 * (hours - 40))
print pay



#
try:
    sos = raw_input ("enter score")
    score = float (sos)
    if score > 1.0:
        print "out of band"
    elif score >= 0.9:
        print "A"
    elif score >= 0.8:
        print "B"
    elif score >= 0.7:
        print "C"
    elif score >= 0.6:
        print "D"
    elif score < 0.6:
        print "F"
except:
    print "invalid number"
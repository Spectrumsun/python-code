#week 4
def computepay (h, r):
    if h <= 40 :
        p = h * r
    else :
        p = rate * 40 + (r  * 1.5 * (h - 40 ))
    return p
try:
    hor = raw_input ("Enter hours")
    hours = float(hor)
    rat = raw_input ("Enter rate")
    rate = float(rat)
except:
    print "enter a number thank you"
    quit()
pay = computepay(hours, rate)
print pay


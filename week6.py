#week 6
data = "X-DSPAM-Confidence:    0.8475"
at = data.find(":")
sppos = data.find("5")
host = data[at+1:sppos+1]
num =float(host)
print num

count = 0
fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.strip()
    jel = pieces.find("@")
    email = pieces[jel+1:]
    count = count + 1
    print  email, count

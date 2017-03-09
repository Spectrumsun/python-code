#week5
largest = None
small = None
while True:
    num = raw_input("enter numbers")   
    if num == "done": break
    try:
        numbers = float(num)
    except:
        print "Invalid input"       
        continue         
    if small is None:
       small = num
    elif num < small:  
        small = num
        continue
    if num > largest:
        largest = num
print "Maximum is", largest
print "Minimum is", small

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    if first<=last:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                alist = alist[0:midpoint]
                return binarySearch(alist,item)
            else:
                alist = alist[midpoint+1:]
                return binarySearch(alist,item)

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 20))
print(binarySearch(testlist, 13))
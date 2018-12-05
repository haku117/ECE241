
def merge2List(alist, lefthalf, righthalf, i, j, pos):

    comparison = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[pos] = righthalf[j]
            j += 1
        else:
            alist[pos] = lefthalf[i]
            i += 1
        comparison += 1
        pos += 1

    while i < len(lefthalf):
        alist[pos] = lefthalf[i]
        i = i + 1
        pos += 1

    while j < len(righthalf):
        alist[pos]=righthalf[j]
        j=j+1
        pos += 1
    return comparison

def mergeSort_3_way(alist):

    comparison = 0

    if len(alist) == 2:
        if alist[0] < alist[1]:
            temp = alist[1]
            alist[1] = alist[0]
            alist[0] = temp
        comparison += 1

    if len(alist)>2:
        mid = len(alist)//3
        leftPart = alist[:mid]
        midPart = alist[mid:mid*2]
        rightPart = alist[mid*2:]

        comparison += mergeSort_3_way(leftPart)
        comparison += mergeSort_3_way(midPart)
        comparison += mergeSort_3_way(rightPart)

        i=0
        j=0
        k=0
        pos = 0

        while i < len(leftPart) and j < len(midPart) and k < len(rightPart):

            # put the largest number in the alist
            if leftPart[i] < midPart[j]:
                if rightPart[k] < midPart[j]:
                    alist[pos] = midPart[j]
                    j += 1
                else:
                    alist[pos] = rightPart[k]
                    k += 1
            else:
                if rightPart[k] < leftPart[i]:
                    alist[pos] = leftPart[i]
                    i += 1
                else:
                    alist[pos] = rightPart[k]
                    k += 1

            pos += 1
            comparison += 2

        if i == len(leftPart):
            comparison += merge2List(alist, midPart, rightPart, j, k, pos)
        elif j == len(midPart):
            comparison += merge2List(alist, leftPart, rightPart, i, k, pos)
        else:
            comparison += merge2List(alist, leftPart, midPart, i, j, pos)

    return comparison




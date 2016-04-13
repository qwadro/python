lst = [6, -1, 5, -17, 3, 9]




maxlist = []
newlst = lst[:-1]

maxlist.append(max(lst))
while(len(lst)>1):

    lst2 = lst[1:]
    for i in range(len(lst)-1):
        newlst[i] += lst2[i]
    lst.pop(0)
    maxlist.append(max(newlst))


print(max(maxlist))

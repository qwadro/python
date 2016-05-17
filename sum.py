lst = [9, -20, 8, 1, 10,-10]

newlst = lst[:-1]
a = max(lst)



while(len(lst)>1):

    lst2 = lst[1:]

    for i in range(len(lst)-1:0:-1):

        newlst[i] += lst[i+1]

    lst.pop(0)

    if a < max(newlst):
    	a = max(newlst)


print(a)


## Given the array of IDs, which contains many duplicate integers and one unique integer, find the unique integer.

#[1,2,3,2,3] -> 1
#[1,2,2,1,1,4,5,1,1,1,4,5,3] -> 3

a = [1,2,2,1,1,4,5,1,1,1,4,5,3]
b = [1,2,3,2,3]



def uniqid(lst):
	
	d = {}
	returnlist = []
	for item in lst:
		if item not in d:	
			d[item] = 1
		else:
			d[item] += 1

	for k, v in d.items():
		if v == 1:
			returnlist.append(k)

	
	return returnlist


print(uniqid(a))
print(uniqid(b))


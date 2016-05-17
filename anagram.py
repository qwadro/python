
## check word for anagramm


def anagramm(lst):
	
	d = {}
	i = 0
	for item in lst:
		if item not in d:	
			d[item] = 1
		else:
			d[item] += 1

	for k, v in d.items():
		if v%2 != 0:
			i+=1
			

	if i <=1:
		return True
	else:
		return False

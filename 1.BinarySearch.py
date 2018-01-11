search=2
ar = [1,2,3,4,5,6,7,8,9]
first=0
last=len(ar)-1
while first <= last:
	i=(first+last)/2
	if ar[i]==search:
		print 'found'
		break
	elif ar[i] > search:
		last=i-1
	else:
		if (first<last):
			first=i+1
		else:
			print "not found"
			break
sample=[8,5,2,9,5,6,3]
#Assume that left most part sorted
#then insert the elements in right at the right place

for i in range(1, len(sample)):
	j=i
	while j>0:
		if sample[j] < sample[j-1]:
			sample[j], sample[j-1] = sample[j-1], sample[j]
			j-=1
		else:
			j-=1
			continue
	print(sample)
print(sample)

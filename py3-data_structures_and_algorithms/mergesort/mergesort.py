import random
def merge(arr,l,m,r):
	left = []
	right = []
	n1 = m-l+1
	n2 = r-m
	for i in range(0,n1):
		left.append(arr[l+i])
		i += 1
	for j in range(0,n2):
		right.append(arr[m+j+1])
		j += 1
	a = 0
	b = 0
	while a<n1 and b<n2:
		if left[a]<=right[b]:
			arr[l]=left[a]
			a += 1
			l += 1
		else:
			arr[l] = right [b]
			b += 1
			l += 1

	while a<n1:
		arr[l] = left[a]
		l += 1
		a += 1

	while b<n2:
		arr[l] = right[b]
		l += 1
		b += 1



def merge_sort(arr,l,r):
	if l<r:
		m= int((l+(r-1))/2)
		merge_sort(arr,l,m)
		merge_sort(arr,m+1,r)
		merge(arr,l,m,r)

array = []

size = int(input("enter the size of the array : "))

for i in range(0,size):
	array.append(random.randint(0,size))

print("before merge_sort :\n",array)
merge_sort(array,0,size-1)
print("after merge_sort :\n",array)
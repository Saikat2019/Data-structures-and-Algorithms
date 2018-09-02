import random
def insertion_sort(arr):
	
	for i in range(1,len(arr)):
		key = arr[i]
		j=i-1
		while j>=0 and key<arr[j]:
			arr[j+1]=arr[j]
			j-= 1
		arr[j+1] = key

arr = []

size = int(input("enter the size of the array : "))

for i in range(0,size):
	arr.append(random.randint(0,size))

print("array before inserting :\n ", arr)
insertion_sort(arr)
print("after inserting : \n",arr)
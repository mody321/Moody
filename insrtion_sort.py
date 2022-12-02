
def insertionSort(arr):

	
	for i in range(1, len(arr)):

		key = arr[i]

		
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key


arr = [17, 1, 13, 6, 20,30,25]
insertionSort(arr)
print(arr)


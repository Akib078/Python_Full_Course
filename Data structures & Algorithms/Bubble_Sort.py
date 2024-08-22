def bubble_sort(array):
    
    size = len(array)

    for i in range(size-1):
        for j in range(size-1):
            if array[j]>array[j+1]:
                temp = array[j]
                array[j]=array[j+1]
                array[j+1]=temp


array = [4,2,7,3,5]

bubble_sort(array)
print("Sorted array is = ",array)

#Time complexcity : O(n²)
def insertion_sort(array):
    size = len(array)

    for i in range(1,size):
        j = i

        while array[j-1] > array[j] and j > 0:
            temp = array[j-1]
            array[j-1]= array[j]
            array[j]= temp

            j = j -1

array = [6,2,4,1,3,5]

insertion_sort(array)
print("Sorted array is = ",array)

#Time complexcity : O(n^2)
def selection_sort(array):
    size = len(array)

    for i in range(size-1):
        min_indx = i

        for j in range(min_indx+1,size):
            if array[j] < array[min_indx]:
                min_indx = j

        temp = array[i]
        array[i] = array[min_indx]
        array[min_indx] = temp

array = [5,2,1,4,3]
selection_sort(array)

print ("Sorted array = ",array)

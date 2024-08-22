def binary_search(numbers_list,number_to_find):
    left_index = 0
    right_index = len(numbers_list)-1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index)//2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:
            left_index = mid_index + 1 

        else:
            right_index = mid_index - 1

    return -1

#Run function
numbers_list = [3,5,7,9,11,13]
number_to_find = 7

index = binary_search(numbers_list,number_to_find)
print(f"Mid number found at index {index} using binary search.")

#Merging two sorted arrays : 

# def merge(a,b):

#     sorted=[]

#     len_a = len(a)
#     len_b = len(b)

#     i = j = 0

#     while i < len_a and j < len_b:
#         if a[i] < b[j]:
#             sorted.append(a[i])
#             i+=1
#         else:
#             sorted.append(b[j])
#             j+=1

#     while i < len_a:
#         sorted.append(a[i])
#         i+=1
#     while j < len_b:
#         sorted.append(b[j])
#         j+=1

#     return sorted


# a = [1,3,5,7]
# b = [2,4,6,8]


# print("Merged = ",merge(a,b))



#Main algorithm

def merge_sort(array):
    if len(array)<=1:
        return array
    mid = len(array)//2

    left_arr = array[:mid]
    right_arr = array[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge_two_sorted_lists(left_arr,right_arr)


        
def merge_two_sorted_lists(a,b):

    sorted=[]

    len_a = len(a)
    len_b = len(b)

    i = j = 0

    while i < len_a and j < len_b:
        if a[i] < b[j]:
            sorted.append(a[i])
            i+=1
        else:
            sorted.append(b[j])
            j+=1

    while i < len_a:
        sorted.append(a[i])
        i+=1
    while j < len_b:
        sorted.append(b[j])
        j+=1

    return sorted


a = [5,10,15,20]
b = [4,8,12,16]


print("Merged = ",merge_two_sorted_lists(a,b))        
def bubble_sort(items):
    ''' Puts a list in increasing order by successively comparing adjacent elements
        interchanging them if they are in the wrong order '''

    for num in range(len(items)-1,0,-1):
        for i in range(num):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items


def merge(list1, list2, final_list):
    '''
    merge sorted lists list1 and list2 into final_list

    '''
    index1=0
    index2=0
    index3=0

    #loop while list1 and list2 have more items
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:       #top element of list1 is smaller
            final_list[index3] = list1[index1]  # copy it into current spot in final_list
            index1 += 1
        else:
            final_list[index3] = list2[index2]
            index2 += 1
        index3 += 1                             # element added to final_list then update position

    # list1 or list2 will be done so one of the following loops
    # will execute to finish the merge

    #copy remaining items from list1 if present
    while index1 < len(list1):
        final_list[index3] = list1[index1]
        index1 += 1
        index3 += 1

    #copy remaining items from list2 if present
    while index2 < len(list2):
        final_list[index3] = list2[index2]
        index2 += 1
        index3 += 1

def merge_sort(items):
    '''
    Return array of items, sorted in ascending order
    by splitting items into two halves
    merge_sort the two halves and merge the sorted halves

    '''
    n = len(items)
    # dont do anything if items has 0 or 1 item
    if n > 1:
        #split into two sublists
        midpoint = n//2
        item1 = items[:midpoint]
        item2 = items[midpoint:]
        # sort each sublist recursively
        merge_sort(item1)
        merge_sort(item2)
        # merge the sorted sublists into the original list items
        merge(item1, item2, items)
    return items



def iquick_sort(S, a, b):

    if a >= b: return # sorting range
    pivot = S[b] # last element of range is pivot
    left = a # will scan on the right
    right = b - 1 # will scan on the left
    while left <= right:
     # scan until reaching value equal or larger than pivot
        while left <= right and S[left] < pivot:
            left += 1
     # scan until reaching value equal or smaller than pivot
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right: # scans did not strictly cross
            S[left], S[right] = S[right], S[left] # swap values
            left, right = left + 1, right - 1 # decrease range

     # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
     # make recursive calls
    iquick_sort(S, a, left - 1)
    iquick_sort(S, left + 1, b)

def quick_sort(S):
    iquick_sort(S, 0, len(S)-1)

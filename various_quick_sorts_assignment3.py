def quick_sort(array, low, high):
    if high - low <= 1:
        return 0 

    else:
        print array
        p = partition_for_sort(array, low, high)
        print p
        quick_sort(array, low, p)
        quick_sort(array,p+1, high)
        return array


def partition_for_sort(array, left, right):
    pivot = array[left]
    i = left + 1

    for j in range(left+1,right):
        if array[j] < pivot:                   
            array[i], array[j] = array[j], array[i]
            i = i + 1           
            
    array[i-1], array[left] = array[left], array[i-1]
    return i-1


def main():
    list_to_sort = [1, 3, 2, 5, 6, 4]
    sorted_list = quick_sort(list_to_sort, 0, len(list_to_sort))
    print sorted_list



if __name__ == "__main__":
    main()
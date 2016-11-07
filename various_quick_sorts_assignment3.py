count = 0

def quick_sort(array, low, high):
    if high - low <= 1:
        return 0 

    else:
        print array
        p = partition_for_sort(array, low, high)
        quick_sort(array, low, p)
        quick_sort(array,p+1, high)
        return array


def partition_for_sort(array, left, right):
    global count
    count += (right - left - 1)
    pivot = array[left]
    i = left + 1
    j = left + 1

    for j in range(j, right):
        if array[j] < pivot:                   
            array[i], array[j] = array[j], array[i]
            i = i + 1           
            
    array[i-1], array[left] = array[left], array[i-1]
    return i-1


def main():
    list_to_sort = [1, 3, 2, 5, 6, 4]
    list_to_sort = [3, 9, 8, 4, 6, 10, 2, 5, 7, 1]
    sorted_list = quick_sort(list_to_sort, 0, len(list_to_sort))
    print sorted_list
    print count



if __name__ == "__main__":
    main()
'''
Count Inversions - Assignment 2

This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.
'''
inversions_count = 0

def sort_and_count_inversions(array, array_len):
    if array_len < 2:
        count_of_inversions = 0 
        sorted_array = array
        return count_of_inversions, sorted_array
    else:
        a1, a2 = split_list(array, array_len)

        a1_inv_count, a1_sorted_list = sort_and_count_inversions(a1, array_len/2)
        a2_inv_count, a2_sorted_list = sort_and_count_inversions(a2, array_len/2)

        split_invs_count, a_sorted = merge_sort_inv_count(a1_sorted_list, a2_sorted_list)

        count_of_inversions = split_invs_count

        return count_of_inversions, a_sorted


def merge_sort_inv_count(a1, a2):   
    i = 0
    j = 0
    global inversions_count
    output_array = []
    
    while (i < len(a1) and j < len(a2)):
        if a1[i] < a2[j]:
            output_array.append(a1[i])
            i += 1

            #add remainder of a2 to the list, if a1 is exhausted
            if i == len(a1) and j != len(a2):
                while (j != len(a2)):
                    output_array.append(a2[j])
                    j += 1

        elif a1[i] > a2[j]:
            output_array.append(a2[j])
            inversions_count += (len(a1)-i)
            j += 1

            #add remainder of a1 to the list, if a2 is exhausted
            if i < len(a1) and j == len(a2):
                while i != len(a1):
                    output_array.append(a1[i])
                    i += 1
        print inversions_count

    return inversions_count, output_array


def split_list(list_to_split, len_a):
    a1, a2 = list_to_split[:len_a/2], list_to_split[len_a/2:]
    return a1, a2

def main():
    array_to_count = [10, 8, 9, 7, 3, 4, 6, 5]
    
    array_len = len(array_to_count)

    final_inversions_count, sorted_array = sort_and_count_inversions(array_to_count, array_len)
    print sorted_array
    print final_inversions_count

if __name__ == "__main__":
    main()

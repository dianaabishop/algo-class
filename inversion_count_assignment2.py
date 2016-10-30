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

        split_invs_count, a_sorted = merge_sort_inv_count(a1_sorted_list, a2_sorted_list, array_len)

        count_of_inversions = a1_inv_count + a2_inv_count + split_invs_count

        return count_of_inversions, a_sorted


def merge_sort_inv_count(a1, a2, len_a):
    len_final_list = len(a1)
    i = 0
    j = 0
    global inversions_count 
    output_array = []
    print a1," ",a2

    while (i < len(a1) and j < len(a2)):
        if a1[i] < a2[j]:
            output_array.append(a1[i])
            i += 1

            if i == len(a1) and j != len(a2):
                while (j != len(a2)):
                    output_array.append(a2[j])
                    j += 1

        elif a1[i] > a2[j]:
            output_array.append(a2[j])
            inversions_count = inversions_count + len(a1[i:])
            j += 1

            if i < len(a1) and j == len(a2):
                while j != len(a1):
                    output_array.append(a1[i])
                    i += 1

    return inversions_count, output_array


def split_list(list_to_split, len_a):
    a1, a2 = list_to_split[:len_a/2], list_to_split[len_a/2:]
    return a1, a2

def main():
    array_to_count = [1, 3, 5, 2, 4, 6]
    array_to_count = [1, 2, 3, 4, 6, 5]
    
    array_len = len(array_to_count)

    final_inversions_count, sorted_array = sort_and_count_inversions(array_to_count, array_len)
    print sorted_array
    print final_inversions_count

if __name__ == "__main__":
    main()

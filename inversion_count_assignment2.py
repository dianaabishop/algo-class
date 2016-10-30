'''
Count Inversions - Assignment 2

This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the ith entry of an array.
Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.
'''


def count_inversions(array, array_len):
	#base case - len(array) < 2
	if array_len < 2:
		inversion_count = 0 
		return inversion_count
	else:
		a1, a2 = split_list(array, array_len)
		a1_inv_count = count_inv(a1)
		a2_inv_count = count_inv(a2)
		split_invs_count = merge_sort_inv_count(a1, a2)
		count_of_inversions = a1_inv_count + a2_inv_count + split_invs_count
		return count_of_inversions

def count_inv(array):
	inversion_count = 0
	idx = 0 
	for a in range(1,len(array)-1):
		if array[idx] > array[idx+1]:
			inversion_count += 1	 
		idx += 1

	return inversion_count

def merge_sort_inv_count(array1, array2):



def split_list(list_to_split, len_a):
	a1, a2 = list_to_split[:len_a/2], list_to_split[len_a/2:]
	return a1, a2

def main():
	array_to_count = [3,5,2,1,6,7,4,8]
	array_len = len(array_to_count)
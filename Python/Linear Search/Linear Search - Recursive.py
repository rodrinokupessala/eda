"""Python Program to Implement Linear Search Recursively"""


def linear_search(arr, key, size):
		# If the array is empty we will return -1

	if size == 0:
		return -1

	# Otherwise if the array consists of only one element and that element is not the one
	# we are searching for then it will also return -1

	elif size == 1 and arr[0] != key:
		return -1

	# ELse , if the element at the size index is same as the element we are searching for
	# Then return the size. This will return the index position is 0 index manner.
	# i.e if the element is present at 6th position it will return 5.
	# To get the exact position in human readble format (counting starts from 1 not 0)
	# Then just return size + 1

	elif arr[size] == key:
		return size

	# If none of the conditions are True then in else condition we will call the
	# function recursively by decreasing the size by 1 each time.

	else:
		return linear_search(arr, key, size-1)

# Driver's code
if __name__ == "__main__":
	arr = [5, 15, 6, 9, 4]
	key = 4
	size = len(arr)-1

	# Calling the Function
	print("The element ", key, " is found at index: ",
		linear_search(arr, key, size), " of given array")


	# Code Contributed By - DwaipayanBandyopadhyay

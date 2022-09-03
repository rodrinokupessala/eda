# python3 program for Implementing
# suffix sum array

# Function to create suffix sum array
def createSuffixSum(arr, n):

	# Create an array to store the suffix sum
	suffixSum = [0 for _ in range(n)]

	# Initialize the last element of
	# suffix sum array with last element
	# of original array
	suffixSum[n - 1] = arr[n - 1]

	# Traverse the array from n-2 to 0
	for i in range(n-2, -1, -1):

		# Adding current element
		# with previous element from back
		suffixSum[i] = suffixSum[i + 1] + arr[i]

	# Return the computed suffixSum array
	return suffixSum

# Driver Code
if __name__ == "__main__":

	arr = [10, 14, 16, 20]
	N = len(arr)

	# Function call to fill suffix sum array
	suffixSum = createSuffixSum(arr, N)

	# Printing the computed suffix sum array
	print("Suffix sum array: ", end="")
	for i in range(0, N):
		print(suffixSum[i], end=" ")

	# This code is contributed by rakeshsahni

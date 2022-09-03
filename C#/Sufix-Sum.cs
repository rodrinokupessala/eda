// C# program for Implementing
// suffix sum array
using System;
class GFG {

// Function to create suffix sum array
static int[] createSuffixSum(int[] arr, int n)
{

	// Create an array to store the suffix sum
	int[] suffixSum = new int[n];

	for (int i = 0; i < n; i++) {
	suffixSum[i] = 0;
	}

	// Initialize the last element of
	// suffix sum array with last element
	// of original array
	suffixSum[n - 1] = arr[n - 1];

	// Traverse the array from n-2 to 0
	for (int i = n - 2; i >= 0; i--)

	// Adding current element
	// with previous element from back
	suffixSum[i] = suffixSum[i + 1] + arr[i];

	// Return the computed suffixSum array
	return suffixSum;
}

// Driver Code
public static void Main()
{
	int[] arr = { 10, 14, 16, 20 };
	int N = arr.Length;

	// Function call to fill suffix sum array
	int[] suffixSum = createSuffixSum(arr, N);

	// Printing the computed suffix sum array
	Console.Write("Suffix sum array: ");
	for (int i = 0; i < N; i++)
	Console.Write(suffixSum[i] + " ");
}
}

// This code is contributed by Samim Hossain Mondal.

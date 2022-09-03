// C++ program for Implementing
// suffix sum array
#include <bits/stdc++.h>
using namespace std;

// Function to create suffix sum array
vector<int> createSuffixSum(vector<int> arr, int n)
{
	// Create an array to store the suffix sum
	vector<int> suffixSum(n, 0);

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
int main()
{
	vector<int> arr = { 10, 14, 16, 20 };
	int N = arr.size();

	// Function call to fill suffix sum array
	vector<int> suffixSum = createSuffixSum(arr, N);

	// Printing the computed suffix sum array
	cout << "Suffix sum array: ";
	for (int i = 0; i < N; i++)
		cout << suffixSum[i] << " ";
}

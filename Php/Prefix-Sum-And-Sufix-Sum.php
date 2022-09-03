<?php
// PHP program for
// Implementing prefix
// sum array

// Fills prefix sum array
function fillPrefixSum($arr,
					$n)
{
	$prefixSum = array();
	$prefixSum[0] = $arr[0];

	// Adding present element
	// with previous element
	for ($i = 1; $i < $n; $i++)
		$prefixSum[$i] = $prefixSum[$i - 1] +
									$arr[$i];
		
	for ($i = 0; $i < $n; $i++)
		echo $prefixSum[$i] . " ";
}

// Driver Code
$arr = array(10, 4, 16, 20);
$n = count($arr);

fillPrefixSum($arr, $n);

// This code is contributed
// by Sam007
?>

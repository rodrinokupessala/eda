<?php
// PHP program to demonstrate use 
// of circular array without using
// extra memory space
 
// function to print circular list 
// starting from given index ind.

function print($a, $n, $ind)
{

    // print from ind-th index 

    // to (n+i)th index.

    for ($i = $ind; $i < $n + $ind; $i++)

        echo $a[($i % $n)] . " ";
}
 
// Driver Code

$a = array( 'A', 'B', 'C', 

            'D', 'E', 'F' );

$n = count($a);
echo "Circular";
print($a, $n, 3);
 
// This code is contributed by Sam007
?>
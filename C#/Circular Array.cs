// C# program to demonstrate use of circular
// array without using extra memory space

using System;
 

public class GfG {
 

    // function to print circular list

    // starting from given index ind.

    public static void print(char[] a, int n,

                                     int ind)

    {

        // print from ind-th index to

        // (n+i)th index.

        for (int i = ind; i < n + ind; i++)

            Console.Write(a[(i % n)] + " ");

    }
 

    // driver code

    public static void Main()

    {

        char[] a = new char[] { 'A', 'B', 'C',

                                'D', 'E', 'F' };

        int n = 6;

        print(a, n, 3);

    }
}
 
/* This code is contributed by vt_m */
 

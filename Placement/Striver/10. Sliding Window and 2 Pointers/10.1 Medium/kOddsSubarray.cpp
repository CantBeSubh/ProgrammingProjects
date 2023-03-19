#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// int soln(int n, vector<int> &nums, int k)
// {
//     int cnt = 0, res = 0;
//     int i = 0, j = 0;
//     while (j < n)
//     {
//         if (nums[j] % 2 != 0)
//             cnt++;
//         if (cnt > k)
//         {
//             while (nums[i] % 2 == 0)
//                 i++;
//             i++;
//             cnt--;
//         }
//         if (cnt == k)
//         {
//             while (nums[j] % 2 == 0)
//             {
//                 j++;
//                 res++;
//             }
//             while (nums[i] % 2 == 0)
//             {
//                 i++;
//                 res++;
//             }
//             res++;
//         }
//         j++;
//     }
//     while (nums[i] % 2 == 0)
//     {
//         i++;
//         res++;
//     }
//     res++;
//     return res;
// }

int soln(vector<int> arr, int n, int m)
{

    int i = 0, ans = 0, odd = 0;
    for (int j = 0; j < n; j++)
    {
        if (arr[j] % 2 == 1)
        {
            odd++;
        }

        /* if count of odd elements is greater than m,
        then increment the i index and check whether
        arr[i] is odd or not*/

        while (odd > m)
        {

            // if arr[i] is odd, then decrement the odd.
            if (arr[i] % 2 == 1)
            {
                odd--;
            }
            // increment the index i
            i++;
        }
        ans += j - i + 1;
    }
    return ans;
}

int countSubarrays(vector<int> arr, int n, int m)
{
    // subract the subarrays with at most k-1 odd elements occur from
    // the subarrays with at most k odd elements occur, we get exactly
    // subarray with k odd elements.

    return soln(arr, n, m) - soln(arr, n, m - 1);
}

int main()
{
    vector<int> nums = {2, 2, 5, 6, 9, 2, 11};
    int k = 2;
    cout << countSubarrays(nums, nums.size(), k) << endl;
    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int MaxSubSum(int arr[], int n, int k)
{
    if (k > n)
        return -1;
    int l = 0, r = k - 1;
    int maxSum = 0;

    for (int i = l; i <= r; i++)
        maxSum += arr[i];

    int sum = maxSum;
    r = k;
    while (r < n)
    {
        sum = sum - arr[l] + arr[r];
        maxSum = max(maxSum, sum);
        l++;
        r++;
    }

    return maxSum;
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k;
    cout << "Enter Subarray Size: ";
    cin >> k;
    cout << MaxSubSum(arr, n, k);
    return 0;
}
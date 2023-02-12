#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void soln(int arr[], int n, int k)
{
    int i = 0;
    int j = 0;
    int m = -1;
    while (j < n)
    {
        if (m < i && arr[j] < 0)
            m = j;
        if (j - i + 1 < k)
            j++;
        else
        {
            cout << arr[m] << " ";
            i++;
            j++;
        }
    }
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int arr[] = {12, -1, -7, 8, -15, 30, 16, 28};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3;
    soln(arr, n, k);
}
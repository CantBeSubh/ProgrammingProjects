#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// THIS TLE DUE TO RECURSION

// int soln(int arr[], int n, int p, int cnt)
// {
//     if (p == n - 1)
//         return cnt;
//     if (p >= n)
//         return INT_MAX;
//     int ans = INT_MAX;
//     for (int i = 1; i <= arr[p]; i++)
//         ans = min(ans, soln(arr, n, p + i, cnt + 1));
//     return ans;
// }

bool soln(int arr[], int n, int p)
{
    if (p == n - 1)
        return true;

    for (int i = 1; i <= arr[p]; i++)
        if (soln(arr, n, p + i))
            return true;
    return false;
}
int canReach(int A[], int N)
{
    int cnt = soln(A, N, 0);
    return cnt;
}
int main()
{
    int A[] = {1, 2, 0, 3, 0, 0};
    cout << canReach(A, 6);
    return 0;
}
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<int> find(int arr[], int n, int x)
{
    int first = -1;
    int last = -1;
    int low = 0;
    int high = n - 1;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr[mid] > x)
        {
            high = mid - 1;
        }
        else if (arr[mid] < x)
        {
            low = mid + 1;
        }
        else
        {
            first = mid;
            high = mid - 1;
        }
    }
    int low = 0;
    int high = n - 1;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (arr[mid] > x)
        {
            high = mid - 1;
        }
        else if (arr[mid] < x)
        {
            low = mid + 1;
        }
        else
        {
            last = mid;
            low = mid + 1;
        }
    }
    return {first, last};
}
int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    int x;
    cin >> x;
    int first = -1;
    int last = -1;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == x)
        {
            if (first == -1)
            {
                first = i;
            }
            last = i;
        }
    }
    cout << first << " " << last << endl;
    return 0;
}
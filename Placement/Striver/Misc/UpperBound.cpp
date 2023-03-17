#include <iostream>
#include <bits/stdc++.h>
using namespace std;
pair<int, int> getFloorAndCeil(int arr[], int n, int x)
{
    int min = -1;
    int max = -1;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] < x)
        {
            if (max == -1)
            {
                max = arr[i];
            }
            else if (arr[i] > max)
            {
                max = arr[i];
            }
        }
        else if (arr[i] > x)
        {
            if (min == -1)
            {
                min = arr[i];
            }
            else if (arr[i] < min)
            {
                min = arr[i];
            }
        }
        else
        {
            min = arr[i];
            max = arr[i];
        }
    }
    pair<int, int> p = {min, max};
    return p;
}

int main()
{
    cout << "Hello World!" << endl;
    int v[] = {85, 24, 40, 10, 66, 16, 6, 54, 93, 42, 6, 98, 49, 100, 98, 23, 59, 48, 17, 56, 64, 94, 77};
    int n = sizeof(v) / sizeof(v[0]);
    int x = 42;
    pair<int, int> p = getFloorAndCeil(v, n, x);
    cout << p.first << " " << p.second << endl;
    return 0;
}
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int *Sort(int arr[])
{
    return arr;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int arr[5] = {1, 3, 5, 4, 2};
    arr = Sort(arr);
    for (auto x : arr)
        cout << x << " ";
}
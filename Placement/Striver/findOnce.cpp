#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int findOnce(int arr[], int n)
{
    int res = 0;
    for (int i = 0; i < n; i++)
        res = res ^ arr[i];
    return res;
}

int main()
{
    cout << "Hello World" << endl;
}
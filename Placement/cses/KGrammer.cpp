#include <iostream>
#include <bits/stdc++.h>

int func(int n, int k)
{
    if (n == 1)
        return 0;
    return func(n - 1, k / 2) ^ k % 2;
}
using namespace std;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout << func(4, 3);
}
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void weirdAlgo(long long n)
{
    cout << n << " ";
    if (n == 1)
        return;
    if (n % 2 == 0)
    {
        weirdAlgo(n / 2);
    }
    else
    {
        weirdAlgo(3 * n + 1);
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    weirdAlgo(n);
    return 0;
}
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int soln(int n, int m)
{
    if (n > m)
        return 0;
    else
        return m - n;
}
int main()
{
    // your code goes here
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n, m;
        cin >> n >> m;
        cout << soln(n, m) << endl;
    }
    return 0;
}

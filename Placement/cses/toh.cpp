#include <iostream>
#include <bits/stdc++.h>
using namespace std;

typedef long long ll; // shorthand for long long

ll toh(int n, int s, int d, int h, int count = 0)
{
    // Your code here
    count++;
    if (n == 1)
    {
        cout << "move disk 1 from rod " << s << " to rod " << d << endl;
        return count;
    }
    count = toh(n - 1, s, h, d, count);
    cout << "move disk " << n << " from rod " << s << " to rod " << d << endl;
    count = toh(n - 1, h, d, s, count);
    return count;
}

int main()
{
    // solution comes here

    // removes bottleneck of cin and cout
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout << toh(3, 1, 3, 2);
}
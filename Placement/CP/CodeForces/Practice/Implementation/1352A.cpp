#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void soln(int x)
{
    string ans = "";
    int cnt = 0, rem, div = 1;
    while (x >= div)
    {
        div *= 10;
        rem = x % div;
        if (rem != 0)
        {
            cnt++;
            if (ans == "")
                ans = to_string(rem);
            else
                ans = to_string(rem) + " " + ans;
        }
        x -= rem;
    }
    ans = to_string(cnt) + "\n" + ans;
    cout << ans << endl;
    return;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int x;
        cin >> x;
        soln(x);
    }
}
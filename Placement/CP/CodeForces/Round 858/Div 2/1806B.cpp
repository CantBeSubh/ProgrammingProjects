#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int soln(vector<int> a, int n)
{
    int res = 0;
    sort(a.begin(), a.end());
    for (int i = 0; i < n; i++)
    {
        if (res < a[i])
            return res;
        if (a[i] == res)
            res++;
    }
    return res;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        vector<int> a;
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            int x;
            cin >> x;
            a.push_back(x);
        }

        for (int i = 0; i < n - 1; i++)
            a[i] += a[i + 1];
        for (auto i : a)
            cout << i << " ";
        cout << endl;
        cout << soln(a, n - 1) << endl;
    }
    return 0;
}
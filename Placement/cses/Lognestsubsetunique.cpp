#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int soln(string a)
{
    int n = a.length();
    int i = 0, j = 0, res = 0;
    map<char, int> m;
    int cnt = 0;
    while (j < n)
    {
        if (m.find(a[j]) == m.end())
        {
            m[a[j]]++;
            cnt++;
        }
        else
        {
            res = max(res, cnt);
            while (m.find(a[j]) != m.end())
            {
                m.erase(a[i]);
                i++;
                cnt--;
            }
            m[a[j]]++;
            cnt++;
        }
        j++;
    }
    return max(res, cnt);
}
int main()
{
    string a = "geeksforgeeks";
    cout << soln(a);
}
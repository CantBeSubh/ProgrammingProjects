#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<string> res;

void soln(int o, int c, string op)
{
    if (o == 0 && c == 0)
    {
        res.push_back(op);
        return;
    }
    if (o == 0)
    {
        string temp;
        for (int i = 0; i < c; i++)
            temp.push_back(')');
        res.push_back(op + temp);
        return;
    }
    if (o == c)
    {
        op += "(";
        soln(o - 1, c, op);
        return;
    }
    soln(o - 1, c, op + "(");
    soln(o, c - 1, op + ")");
    return;
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    soln(n, n, "");
    for (auto i : res)
        cout << i << endl;
}
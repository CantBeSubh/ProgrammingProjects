#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<string> res;

void soln(string ip, string op)
{
    if (ip.length() == 0)
    {
        res.push_back(op);
        return;
    }
    string op1 = op;
    string op2 = op;
    op2.push_back(ip[0]);
    ip.erase(ip.begin() + 0);
    soln(ip, op1);
    soln(ip, op2);
    return;
}
int main()
{
    string ip;
    cin >> ip;
    string op = "";
    soln(ip, op);
    sort(res.begin(), res.end());
    res.erase(unique(res.begin(), res.end()), res.end());

    // res.erase(res.begin() + 0);
    for (int i = 0; i < res.size(); i++)
    {
        cout << res[i] << " ";
    }
    return 0;
}
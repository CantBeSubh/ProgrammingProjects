#include <iostream>
#include <bits/stdc++.h>

using namespace std;
bool cmp(string a, string b)
{
    a = a.substr(0, a.size() - 1);
    b = b.substr(0, b.size() - 1);
    int x = stoi(a);
    int y = stoi(b);
    return x < y;
}

int soln(int start[], int end[], int n)
{

    vector<string> v;
    for (int i = 0; i < n; i++)
    {
        v.push_back(to_string(start[i]) + "a");
        v.push_back(to_string(end[i]) + "d");
    }
    sort(v.begin(), v.end(), cmp);
    int i = 0, j = 1;
    int res = 0;
    for (auto i : v)
        cout << i << " ";
    while (j < v.size())
    {
        if ((v[i][v[i].size() - 1] == 'a' && v[j][v[i].size() - 1] == 'd') &&
            (v[i].substr(0, v[i].size() - 1) != v[j].substr(0, v[j].size() - 1)))
        {
            res++;
            cout << v[i] << " " << v[j] << endl;
        }
        i++;
        j++;
    }
    return res;
}
int main()
{
    int start[] = {48, 43, 61, 54, 99, 84, 3, 3, 59, 30, 45, 72, 24, 87, 21, 48, 54, 88, 8, 67, 41, 64, 87, 54, 5, 62, 87, 33, 74, 92};
    int end[] = {150, 67, 137, 131, 139, 115, 49, 6, 117, 126, 59, 109, 27, 96, 73, 60, 99, 108, 50, 145, 68, 104, 102, 82, 7, 126, 118, 93, 148, 150};
    cout << soln(start, end, 30);
    return 0;
}
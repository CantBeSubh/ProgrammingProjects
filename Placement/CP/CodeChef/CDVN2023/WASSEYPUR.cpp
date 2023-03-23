#include <iostream>
#include <bits/stdc++.h>

using namespace std;

string soln(map<int, int> SA, map<int, int> RA, vector<pair<int, int>> r)
{
    int s1, s2;
    s1 = SA.size();
    s2 = RA.size();
    for (auto it : r)
    {
        int i = it.first;
        int j = it.second;
        if ((i ^ j) % 2 == 1)
        {
            RA.erase(j);
            s2--;
        }
        else
        {
            SA.erase(i);
            s1--;
        }
        if (s1 == 0 || s2 == 0)
            break;
    }

    if (s1 >= s2)
        return "Sardar";
    else
        return "Ramadhir";
}
int main()
{
    // your code goes here
    int n, x, y;
    cin >> n;
    map<int, int> SA;
    for (int i = 0; i < n; i++)
    {
        cin >> x;
        SA[x]++;
    }
    cin >> n;
    map<int, int> RA;
    for (int i = 0; i < n; i++)
    {
        cin >> x;
        RA[x]++;
    }
    cin >> n;
    vector<pair<int, int>> r;
    for (int i = 0; i < n; i++)
    {
        cin >> x >> y;
        r.push_back({x, y});
    }

    cout << soln(SA, RA, r) << endl;
    return 0;
}
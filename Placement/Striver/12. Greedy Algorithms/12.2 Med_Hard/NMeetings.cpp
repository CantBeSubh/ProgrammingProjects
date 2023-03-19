#include <iostream>
#include <bits/stdc++.h>

using namespace std;
struct Meet
{
    int start;
    int end;
    int pos;
};

bool cmp(Meet a, Meet b)
{
    if (a.end == b.end)
        return a.pos < b.pos;
    return a.end < b.end;
}

int soln(int start[], int end[], int n)
{
    vector<Meet> m(n);
    for (int i = 0; i < n; i++)
    {
        m[i].start = start[i];
        m[i].end = end[i];
        m[i].pos = i + 1;
    }
    sort(m.begin(), m.end(), cmp);
    int ans = 0;
    int prev = -1;
    for (int i = 0; i < n; i++)
    {
        if (m[i].start > prev)
        {
            ans++;
            prev = m[i].end;
        }
    }
    return ans;
}
int main()
{
    int start[] = {1, 3, 0, 5, 8, 5};
    int end[] = {2, 4, 6, 7, 9, 9};
    cout << soln(start, end, 6);
    return 0;
}
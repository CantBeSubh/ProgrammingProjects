#include <iostream>
#include <bits/stdc++.h>

using namespace std;
int soln(int N, int M, vector<int> &greed, vector<int> &sz)
{
    sort(greed.begin(), greed.end());
    sort(sz.begin(), sz.end());
    int i = 0, j = 0;
    while (i < N && j < M)
    {
        if (greed[i] <= sz[j])
            i++;
        j++;
    }
    return i;
}

int main()
{
    vector<int> greed = {1, 2, 3};
    vector<int> sz = {1, 1};
    int N = greed.size();
    int M = sz.size();
    cout << soln(N, M, greed, sz) << endl;
    return 0;
}
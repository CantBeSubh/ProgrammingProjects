#include <iostream>
#include <bits/stdc++.h>

using namespace std;

vector<int> soln(int N)
{
    int arr[] = {1, 2, 5, 10, 20, 50, 100, 200, 500, 2000};
    vector<int> ans;
    sort(arr, arr + 10, greater<int>());
    for (auto i : arr)
    {
        while (N >= i)
        {
            N -= i;
            ans.push_back(i);
        }
    }
    return ans;
}

int main()
{
    vector<int> ans = soln(43);
    for (auto i : ans)
        cout << i << " ";
    return 0;
}
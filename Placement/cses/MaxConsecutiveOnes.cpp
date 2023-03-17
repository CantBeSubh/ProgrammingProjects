#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int soln(int n, vector<int> arr, int k)
{
    int i = 0, j = 0, res = 0;
    int cnt = 0;
    while (j < n)
    {
        if (arr[j] == 0)
            cnt++;

        if (cnt > k)
        {
            while (cnt > k)
            {
                if (arr[i] == 0)
                {
                    cnt--;
                }
                i++;
            }
        }
        res = max(res, j - i + 1);
        j++;
    }
    return res;
}

int main()
{
    vector<int> a = {1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0};
    int k = 2;
    cout << soln(a.size(), a, 2);
    return 0;
}

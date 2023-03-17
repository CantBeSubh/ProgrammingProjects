#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int soln(int n, vector<int> arr)
{
    int i = 0, j = 0;
    int cnt = 0;
    int res = 0;
    map<int, int> m;
    while (j < n)
    {
        if (m.find(arr[j]) == m.end())
        {
            res = max(res, j - i);
            while (cnt == 2)
            {
                m[arr[i]]--;
                i++;
                if (m[arr[i]] == 0)
                {
                    m.erase(arr[i]);
                    cnt--;
                }
            }
            cnt++;
        }
        m[arr[j]]++;
        j++;

        // if (m.find(arr[j]) != m.end())
        // {
        //     m[arr[j]]++;
        //     j++;
        // }
        // else
        // {
        //     if (cnt < 2)
        //     {
        //         m[arr[j]]++;
        //         cnt++;
        //         j++;
        //     }
        //     else
        //     {
        //         res = max(res, j - i);
        //         while (cnt == 2)
        //         {
        //             m[arr[i]]--;
        //             if (m[arr[i]] == 0)
        //             {
        //                 m.erase(arr[i]);
        //                 cnt--;
        //             }
        //             i++;
        //         }
        //         m[arr[j]]++;
        //         cnt++;
        //         j++;
        //     }
        // }
    }
    res = max(res, j - i);
    return res;
}

int main()
{
    vector<int> a = {0, 1, 2, 2, 2, 2};
    int k = 2;
    cout << soln(a.size(), a);
    return 0;
}

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string inp;
    cin >> inp;
    int flag = 1;
    for (auto i : inp)
    {
        int x = int(i - '0');
        if (flag == 1)
        {
            if (x == 9)
                cout << x;
            else if (x > 4)
                cout << 9 - x;
            else
                cout << x;
            flag = 0;
        }

        else
        {
            if (x > 4)
                cout << 9 - x;
            else
                cout << x;
        }
    }
    return 0;
}
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int soln()
{
    int i, j, x;
    for (i = 0; i < 5; i++)
    {
        x = 0;
        for (j = 0; j < 5; j++)
        {
            cin >> x;
            if (x == 1)
                return abs(i - 2) + abs(j - 2);
        }
    }
    return 0;
}
int main()
{
    cout << soln();
    return 0;
}
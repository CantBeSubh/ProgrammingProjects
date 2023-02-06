#include <bits/stdc++.h>
#include <iostream>
using namespace std;

bool isPallindrome(string str)
{
    int i = 0;
    int j = str.length() - 1;
    while (i < j)
    {
        if (str[i] != str[j])
        {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

int min(int a, int b)
{
    return a < b ? a : b;
}

void soln(vector<string> op, string ip, int &res)
{
    if (ip.length() == 0)
    {
        res = min(res, op.size());
        return;
    }
}
int palindromicPartition(string str)
{
    return 0;
}

int main()
{
    return 0;
}
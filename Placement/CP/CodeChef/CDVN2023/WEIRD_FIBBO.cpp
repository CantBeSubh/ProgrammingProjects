#include <iostream>
#include <bits/stdc++.h>

using namespace std;
string bin(long long N)
{
    string s = "";
    while (N > 0)
    {
        s = (N % 2 == 0 ? "0" : "1") + s;
        N = N / 2;
    }
    return s;
}

long long Num(string s)
{
    long long n = 0;
    for (long long i = 0; i < s.length(); i++)
    {
        n = n * 2 + (s[i] - '0');
    }
    return n;
}

string nI(string s)
{
    long long c0 = 0, c1 = 0;
    for (long long i = 0; i < s.length(); i++)
    {
        if (s[i] == '0')
            c0++;
        else
            c1++;
    }
    string s1 = "";
    for (long long i = 0; i < c1; i++)
        s1 += '1';
    for (long long i = 0; i < c0; i++)
        s1 += '0';
    return s1;
}
string nD(string s)
{
    long long c0 = 0, c1 = 0;
    for (long long i = 0; i < s.length(); i++)
    {
        if (s[i] == '0')
            c0++;
        else
            c1++;
    }
    string s1 = "";
    for (long long i = 0; i < c0; i++)
        s1 += '0';
    for (long long i = 0; i < c1; i++)
        s1 += '1';
    return s1;
}

long long F(long long a, long long b, long long n)
{
    if (n == 0)
        return a;
    if (n == 1)
        return b;
    string l = nI(bin(F(a, b, n - 2)));
    string r = nD(bin(F(a, b, n - 1)));
    return Num(l + r);
}

long long soln(long long a, long long b, long long n)
{
    long long res = F(a, b, n);
    long long div = pow(10, 9) + 7;
    return res % div;
}
long long main()
{
    // your code goes here
    long long t;
    cin >> t;
    for (long long i = 0; i < t; i++)
    {
        long long a, b, n;
        cin >> a >> b >> n;
        cout << soln(a, b, n) << endl;
    }
    return 0;
}

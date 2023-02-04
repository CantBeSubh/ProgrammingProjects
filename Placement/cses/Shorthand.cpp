#include <iostream>
#include <bits/stdc++.h>

typedef long long ll; // shorthand for long long
typedef vector<int> vi;
typedef pair<int, int> pi;

#define F first
#define S second
#define PB push_back
#define MP make_pair
#define FOR(i, a, b) for (int i = a; i <= b; i++)

using namespace std;
int main()
{
    // v.push_back(make_pair(y1,x1));
    // v.push_back(make_pair(y2,x2));
    // int d = v[i].first+v[i].second;
    vi v;
    int x1, x2, y1, y2, i;
    v.PB(MP(y1, x1));
    v.PB(MP(y2, x2));
    int d = v[i].F + v[i].S;
}
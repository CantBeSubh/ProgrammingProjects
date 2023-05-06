#include <iostream>

using namespace std;
int soln(string s)
{
    string codeforces = "codeforces";
    if (s.compare(codeforces) == 0)
        return 0;
    int cnt = 0;
    for (int i = 0; i < 10; i++)
        if (s.at(i) != codeforces.at(i))
            cnt++;
    return cnt;
}
int main()
{
    int t;
    string s;
    cin >> t;
    while (t--)
    {
        cin >> s;
        cout << soln(s) << endl;
    }
}
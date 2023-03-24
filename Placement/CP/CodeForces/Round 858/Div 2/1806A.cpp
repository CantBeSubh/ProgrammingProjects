#include <iostream>

using namespace std;
int soln(int x1, int y1, int x2, int y2)
{
    int x = x2 - x1, y = y2 - y1;
    if (y < 0)
        return -1;
    if (x > y)
        return -1;
    return 2 * y - x;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        cout << soln(x1, y1, x2, y2) << endl;
    }
    return 0;
}
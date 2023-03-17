#include <iostream>
#include <bits/stdc++.h>

using namespace std;

struct Item
{
    int value;
    int weight;
};

// double soln(int W, Item arr[], int n)
// {
//     vector<double> ratio(n);
//     for (int i = 0; i < n; i++)
//         ratio[i] = (double)arr[i].value / arr[i].weight;

//     map<double, int, greater<int>> m;
//     for (int i = 0; i < n; i++)
//         m[ratio[i]] += arr[i].weight;

//     double ans = 0;
//     int w = 0;
//     for (auto i : m)
//     {
//         if (w + i.second <= W)
//         {
//             ans += i.first * i.second;
//             w += i.second;
//         }
//         else
//         {
//             ans += i.first * (W - w);
//             break;
//         }
//     }
//     return ans;
// }
bool cmp(Item a, Item b)
{
    return (double)a.value / a.weight > (double)b.value / b.weight;
}

double soln(int W, Item arr[], int n)
{

    // sort(arr, arr + n, [](Item a, Item b){ return (double)a.value / a.weight > (double)b.value / b.weight; });
    sort(arr, arr + n, cmp);
    double ans = 0;
    int w = 0;
    for (int i = 0; i < n; i++)
    {
        if (w + arr[i].weight <= W)
        {
            ans += arr[i].value;
            w += arr[i].weight;
        }
        else
        {
            ans += (double)arr[i].value / arr[i].weight * (W - w);
            break;
        }
    }
    return ans;
}

int main()
{
    int W = 50;
    Item arr[] = {{60, 10}, {100, 20}, {120, 30}};
    cout << soln(W, arr, 3);
    return 0;
}
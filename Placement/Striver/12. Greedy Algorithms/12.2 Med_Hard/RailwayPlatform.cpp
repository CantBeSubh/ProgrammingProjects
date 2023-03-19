#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// struct Train
// {
//     int arrival;
//     int departure;
// };

// bool cmp(Train a, Train b)
// {
//     return a.departure < b.departure;
// }

// int soln(int arr[], int dep[], int n)
// {
//     vector<int> track;
//     vector<Train> trains;
//     for (int i = 0; i < n; i++)
//         trains.push_back({arr[i], dep[i]});
//     sort(trains.begin(), trains.end(), cmp);
//     for (auto i : trains)
//     {
//         if (track.empty())
//             track.push_back(i.departure);
//         else
//         {
//             int j;
//             for (j = 0; j < track.size(); j++)
//             {
//                 if (i.arrival > track[j])
//                 {
//                     track[j] = i.departure;
//                     break;
//                 }
//             }
//             if (j == track.size())
//                 track.push_back(i.departure);
//         }
//     }
//     return track.size();
// }
int soln(int arr[], int dep[], int n)
{
    sort(arr, arr + n);
    sort(dep, dep + n);
    int plat = 0, res = 0;
    int j = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] <= dep[j])
            plat++;
        else
            j++;
        res = max(res, plat);
    }
    return res;
}
int main()
{
    int arr[] = {900, 1100, 1235};
    int dep[] = {1000, 1200, 1240};
    cout << soln(arr, dep, 3);
    return 0;
}
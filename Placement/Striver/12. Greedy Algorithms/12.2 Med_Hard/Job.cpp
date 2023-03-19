#include <iostream>
#include <bits/stdc++.h>

using namespace std;
struct Job
{
    int id;     // Job Id
    int dead;   // Deadline of job
    int profit; // Profit if job is over before or on deadline
};
vector<int> soln(Job arr[], int n)
{

    return {0, 0};
}

int main()
{
    Job arr[] = {(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)};
    int n = sizeof(arr) / sizeof(arr[0]);
    vector<int> res = soln(arr, n);
    cout << res[0] << " " << res[1];
    return 0;
}
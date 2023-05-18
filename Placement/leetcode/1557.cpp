#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> findSmallestSetOfVertices(int n, vector<vector<int>> &edges)
{
    vector<int> ans(n);
    for (int i = 0; i < n; i++)
        ans[i] = i;
    vector<int> reachable(n, 0);

    for (auto edge : edges)
    {
        auto it = find(ans.begin(), ans.end(), edge.at(1));
        if (it != ans.end())
            ans.erase(it);
        reachable[edge.at(1)] = 1;
    }

    for (int i : ans)
        reachable[i] = 1;

    for (int i = 0; i < n; i++)
        if (reachable[i] == 0)
            ans.push_back(i);

    return ans;
}

int main()
{
    int n = 6;
    vector<vector<int>> edges = {{0, 1}, {0, 2}, {2, 5}, {3, 4}, {4, 2}};
    vector<int> result = findSmallestSetOfVertices(n, edges);

    for (int i : result)
        cout << i << " ";
    cout << endl;

    return 0;
}
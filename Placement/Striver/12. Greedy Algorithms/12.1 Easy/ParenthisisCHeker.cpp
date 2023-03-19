#include <iostream>
#include <bits/stdc++.h>

using namespace std;
bool soln(string x)
{
    stack<char> s;
    int i = 0;
    while (i < x.length())
    {
        switch (x[i])
        {
        case '(':
            s.push(x[i]);
            break;
        case ')':
            if (s.empty() || s.top() != '(')
                return false;
            s.pop();
            break;
        case '{':
            s.push(x[i]);
            break;
        case '}':
            if (s.empty() || s.top() != '{')
                return false;
            s.pop();
            break;
        case '[':
            s.push(x[i]);
            break;
        case ']':
            if (s.empty() || s.top() != '[')
                return false;
            s.pop();
            break;
        default:
            return false;
        }
        i++;
    }

    return s.empty();
}
int main()
{
    string x = "()";
    cout << (soln(x) ? "True" : "False");
    return 0;
}
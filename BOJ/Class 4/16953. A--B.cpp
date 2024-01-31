#include <iostream>
#include <string>
#include <queue>
#define MAX 2147483647
using namespace std;


int solution(int a, int b) {
    queue<pair<int, int>> q;
    q.push({a, 1});
    while (!q.empty()) {
        int cur = q.front().first;
        int dist = q.front().second;
        q.pop();
        if (cur <= (MAX / 2) && cur * 2 < b)
            q.push({cur * 2, dist + 1});
        if (cur <= (MAX / 2) && cur * 2 == b) {
            return dist + 1;
        }

        if (cur <= (MAX / 10) && stoi(to_string(cur) + "1") < b)
            q.push({stoi(to_string(cur) + "1"), dist + 1});
        if (cur <= (MAX / 10) && stoi(to_string(cur) + "1") == b) {
            return dist + 1;
        }
    }
    return -1;
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << solution(a, b) << "\n";
}
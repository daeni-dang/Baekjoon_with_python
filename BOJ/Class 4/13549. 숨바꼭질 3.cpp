#include <iostream>
#include <queue>
#include <vector>
#define INF 1e9
using namespace std;

int N, K;

int bfs() {
    queue<int> q;
    vector<int> dist(200001, INF);
    q.push(N);
    dist[N] = 0;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        if (cur == K) {
            return dist[K];
        }
        if (cur * 2 <= K * 2) {
            if (dist[cur] < dist[cur * 2]) {
                dist[cur * 2] = dist[cur];
                q.push(cur * 2);
            }
        }
        if (cur + 1 <= K) {
            if (dist[cur] + 1 < dist[cur + 1]) {
                dist[cur + 1] = dist[cur] + 1;
                q.push(cur + 1);
            }
        }
        if (cur - 1 > -1) {
            if (dist[cur] + 1 < dist[cur - 1]) {
                dist[cur - 1] = dist[cur] + 1;
                q.push(cur - 1);
            }
        }
    }
    return dist[K];
}

int main() {
    cin >> N >> K;
    cout << bfs() << "\n";
}
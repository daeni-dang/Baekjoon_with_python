#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int n;
vector<vector<pair<int, int>>> graph;

pair<int, int> max(vector<pair<int, int>> v) {
    pair<int, int> result = {0, 0};
    for (int i=0; i<v.size(); i++) {
        if (result.first < v[i].first) {
            result = v[i];
        }
    }
    return result;
}

pair<int, int> dijkstra(int start) {
    vector<int> visited(n + 1, 0);
    priority_queue<pair<int, int>> q;
    vector<pair<int, int>> dist(n + 1); // dist, node
    q.push({0, start});
    dist[start] = {0, 0};
    visited[start] = 1;
    while (!q.empty()) {
        int cost = q.top().first;
        int node = q.top().second;
        q.pop();
        if (dist[node].first > cost) continue;
        for (int i=0; i<graph[node].size(); i++) {
            int ncost = graph[node][i].first;
            int nnode = graph[node][i].second;
            if (!visited[nnode]) {
                visited[nnode] = 1;
                if (ncost + cost > dist[nnode].first) {
                    dist[nnode] = {ncost + cost, nnode};
                    q.push({ncost + cost, nnode});
                }
            }
        }
    }
    return max(dist);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    graph.resize(n + 1);
    for (int i=0; i<n-1; i++) {
        int p, c, w;
        cin >> p >> c >> w;
        graph[p].push_back({w, c});
        graph[c].push_back({w, p});
    }
    int answer = 0;
    // 1번 노드에서 가장 먼 노드와 거리 찾기
    pair<int, int> result1 = dijkstra(1);
    pair<int, int> result2 = dijkstra(result1.second);
    answer = result2.first;
    cout << answer << "\n";
}
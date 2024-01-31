#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int board[500][500];
bool visited[500][500];
int n, m;
int answer = 0;

void check_aou(int x, int y) {
    // ㅏ
    if (x - 1 >= 0 && x + 1 < n && y - 1 >= 0 && y + 1 < n) {
        answer = max(answer, board[x][y] + board[x - 1][y] + board[x][y + 1] + board[x + 1][y]);
    }
    // ㅗ
    if (x - 1 >= 0 && x + 1 < n && y - 1 >= 0 && y + 1 < n) {
        answer = max(answer, board[x][y] + board[x - 1][y] + board[x][y + 1] + board[x][y - 1]);
    }
    // ㅓ
    if (x - 1 >= 0 && x + 1 < n && y - 1 >= 0 && y + 1 < n) {
        answer = max(answer, board[x][y] + board[x - 1][y] + board[x][y - 1] + board[x + 1][y]);
    }
    // ㅜ
    if (x - 1 >= 0 && x + 1 < n && y - 1 >= 0 && y + 1 < n) {
        answer = max(answer, board[x][y] + board[x + 1][y] + board[x][y + 1] + board[x][y - 1]);
    }
}

void dfs(int x, int y, int depth, int cnt) {
    int dx[] = {0, 0, 1, -1};
    int dy[] = {1, -1, 0, 0};
    if (depth == 3) {
        answer = max(answer, cnt);
        return;
    }
    for (int i=0; i<4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        
        if (nx >= n || nx < 0 || ny >= m || ny < 0) {
            continue;
        }
        if (!visited[nx][ny]) {
            visited[nx][ny] = true;
            dfs(nx, ny, depth + 1, cnt + board[nx][ny]);
            visited[nx][ny] = false;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> board[i][j];
        }
    }
    memset(visited, false, sizeof(visited));
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            check_aou(i, j);
            visited[i][j] = true;
            dfs(i, j, 0, board[i][j]);
            visited[i][j] = false;
        }
    }
    cout << answer << "\n";
}
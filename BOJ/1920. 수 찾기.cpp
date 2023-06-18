#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n, m;
    unordered_map<int, bool> A;
    cin >> n;
    for (int i=0; i<n; i++) {
        int a;
        cin >> a;
        A[a] = true;
    }
    cin >> m;
    for (int i=0; i<m; i++) {
        int b;
        cin >> b;
        cout << A[b] << "\n";
    }
}
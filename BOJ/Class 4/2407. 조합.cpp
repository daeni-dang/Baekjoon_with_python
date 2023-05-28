#include <iostream>
#include <vector>
#include <string>
using namespace std;

string stringSum(string a, string b) {
    int len = max(a.size(), b.size());
    string result = "";
    int up = 0;
    for (int i=0; i<len; i++) {
        int sum = 0;
        if (!a.empty()) {
            sum += int(a.back() - '0');
            a.pop_back();
        }
        if (!b.empty()) {
            sum += int(b.back() - '0');
            b.pop_back();
        }
        if (up > 0) {
            up--;
            sum += 1;
        }
        if (sum >= 10) {
            up++;
            sum -= 10;
        }
        result += to_string(sum);
    }
    if (up > 0) {
        result += "1";
    }
    string tmp = result;
    for (int i=0; i<tmp.size(); i++) {
        result[i] = tmp[tmp.size() - i - 1];
    }
    return result;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<string>> tri(n+1, vector<string>(n+1, "0"));
    for (int i=0; i<n; i++) {
        tri[i][0] = "1";
    }
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=n; j++) {
            tri[i][j] = stringSum(tri[i - 1][j], tri[i - 1][j - 1]);
        }
    }
    cout << tri[n][m] << "\n";
}
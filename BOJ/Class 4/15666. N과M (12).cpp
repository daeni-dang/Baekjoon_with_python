#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int n, m;
vector<int> num;
vector<int> arr;
set<vector<int>> answer;

void back(int depth) {
    if (depth == m) {
        vector<int> tmp;
        for (int i=0; i<arr.size(); i++) {
            tmp.push_back(arr[i]);
        }
        answer.insert(tmp);
        return;
    }
    for (int i=0; i<num.size(); i++) {
        if (arr.size() == 0 || num[i] >= arr.back()) {
            arr.push_back(num[i]);
            back(depth + 1);
            arr.pop_back();
        }
    }
}

int main() {
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        int x;
        cin >> x;
        num.push_back(x);
    }
    sort(num.begin(), num.end());
    back(0);
    for (auto i : answer) {
        for (int j=0; j<i.size(); j++) {
            cout << i[j] << " ";
        }
        cout << "\n";
    }
}
//  341. Палеты

#include <iostream>
#include <queue>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> delivery(n);
    for (int i = 0; i < n; i++) {
        cin >> delivery[i];
    }
    vector<int> parents(n);
    for (int i = 0; i < n; i++) {
        cin >> parents[i];
    }
    
    int k;
    cin >> k;
    set<int> s;
    if (k > 0) {
        for (int i = 0; i < k; i++) {
            int x;
            cin >> x;
            s.insert(x);
        }
    }
    
    queue<int> q1;
    vector<int> ans;
    for (int i = 0; i < delivery.size(); i++) {
        if (s.find(delivery[i]) != s.end()) {
            delivery[i] = -1;
        }
    }
    
    set<int> pallets;
    vector<set<int>> sons(n);
    
    for (int i = 0; i < parents.size(); i++) {
        if (parents[i] == 0) {
            pallets.insert(i);
            q1.push(i);
        }
        else {
            sons[parents[i] - 1].insert(i);
        }
    }
    
    while (!q1.empty()) {
        int current = q1.front();
        q1.pop();
        for (auto son : sons[current]) {
            q1.push(son);
            if (delivery[current] == -1 || delivery[son] == -1) {
                delivery[current] = -1;
                delivery[son] = -1;
            }
        }
    }
    
    for (auto pallet : pallets) {
        bool flag = false;
        queue<int> q2;
        q2.push(pallet);
        while (!q2.empty()) {
            int current = q2.front();
            q2.pop();
            if (delivery[current] == -1) {
                flag = true;
                break;
            }
            else {
                for (auto tmp : sons[current]) {
                    q2.push(tmp);
                }
            }
        }
        if (!flag) {
            ans.push_back(pallet);
        }
    }
    
    cout << ans.size() << endl;
    sort(ans.begin(), ans.end());
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] + 1 << " ";
    }
    
    return 0;
}
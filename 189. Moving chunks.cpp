//  189. Перемещение чанков

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
    int n, m, q;
    set<pair<int, int>> interval_to_server;
    int mas[100000 + 2];
    cin >> n >> m >> q;
    for (int i = 1; i <= n; ++i) {
        cin >> mas[i];
    }

    interval_to_server.insert({0, INT_MAX});
    interval_to_server.insert({n + 1, INT_MAX});

    for (int i = 1; i <= n; ++i) {
        if (i == n || mas[i] != mas[i + 1]) {
            interval_to_server.insert({i, mas[i]});
        }
    }
    for (int i = 0; i < q; ++i) {
        int a, b, l, r;
        cin >> a >> b >> l >> r;
        
        auto left = interval_to_server.upper_bound({l, 0});
        auto right = interval_to_server.upper_bound({r, 0});

        if (left == right && left->second == a) {
            if ((--left)->first + 1 != l) {
                interval_to_server.insert({l - 1, a});
            }
            if (left->first + 1 == l && left->second == b) {
                interval_to_server.erase(left);
            }
            if (right->first == r) {
                if ((++right)->second == b) {
                    r = right->first;
                }
                interval_to_server.erase(--right);
            }
            interval_to_server.insert({r, b});
            cout << 1 << endl;
        } 
        else {
            cout << 0 << endl;
        }
    }
    return 0;
}
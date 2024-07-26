//  194. Разделение графа

#include <iostream>
#include <vector>
#include <queue>
using namespace std;
using Lint = long long int;

bool check(Lint current, Lint n, vector<vector<pair<Lint, Lint>>>& graph) {
    vector<Lint> visited(n + 1, -1);
    for (Lint a = 1; a <= n; a++) {
        if (visited[a] == -1) {
            visited[a] = 0;
            queue<int> q;
            q.push(a);
            while (!q.empty()) {
                int tmp = q.front();
                q.pop();
                for (auto& edge : graph[tmp]) {
                    int b = edge.first;
                    int w = edge.second;
                    if (w <= current) {
                        if (visited[b] == -1) {
                            q.push(b);
                            visited[b] = 1 - visited[tmp];
                        } else {
                            if (visited[tmp] == visited[b]) {
                                return true;
                            }
                        }
                    }
                }
            }
        }
    }
    return false;
}

Lint left_bin_search(Lint l, Lint r, Lint n, vector<vector<pair<Lint, Lint>>>& graph) {
    while (l < r) {
        int current = (l + r) / 2;
        if (check(current, n, graph)) {
            r = current;
        } else {
            l = current + 1;
        }
    }
    return l;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<pair<Lint, Lint>>> graph(n + 1);
    Lint max_weight = 0;
    for (int i = 0; i < m; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        graph[a].push_back(make_pair(b, w));
        graph[b].push_back(make_pair(a, w));
        if (max_weight < w) {
            max_weight = w;
        }
    }

    Lint l = 1;
    Lint r = max_weight;

    cout << left_bin_search(l, r, n, graph) << endl;

    return 0;
}
#include <iostream>
#include <vector>
#include <climits>
#include <tuple>

using namespace std;

void solution() {
    int n, m;
    cin >> n >> m;
    vector<tuple<int, int, int>> graph;

    for (int i = 0; i < m; i++) {
        int v, u, w;
        cin >> v >> u >> w;
        graph.push_back(make_tuple(v, u, w));
    }

    vector<int> dist(n + 1, 30000);
    dist[1] = 0;

    for (int i = 0; i < n - 1; i++) {
        for (const auto& edge : graph) {
            int u, v, w;
            tie(u, v, w) = edge;

            if (dist[u] != 30000 && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        cout << dist[i] << " ";
    }
}

int main() {
    solution();
    return 0;
}

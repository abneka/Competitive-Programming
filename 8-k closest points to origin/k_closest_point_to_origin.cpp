class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<vector<int>> result;
        priority_queue<pair<int, pair<int,int>>> pq;
        for (int i=0; i < k; i++) {
            int x=points[i][0], y=points[i][1];
            int distance = x*x+y*y;
            pq.push(make_pair(distance, make_pair(x,y)));
        }
        for (int i=k; i<points.size(); i++) {
            int x=points[i][0], y=points[i][1];
            int distance = x*x+y*y;
            if (pq.top().first > distance) {
                pq.pop();
                pq.push(make_pair(distance, make_pair(x,y)));
            }
        }
        while(!pq.empty()) {
            result.push_back({pq.top().second.first, pq.top().second.second});
            pq.pop();
        }
        return result;
    }
};

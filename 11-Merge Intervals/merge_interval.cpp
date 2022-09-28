class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> result;
        sort (intervals.begin(), intervals.end());
        result.push_back(intervals[0]);
        for (int i=1; i< intervals.size(); i ++) {
            if (result.back()[1] >= intervals[i][0]) {
                if (result.back()[1] < intervals[i][1]) result.back() = {result.back()[0], intervals[i][1]};
                else continue;
            }
            else result.push_back(intervals[i]);
        }
        return result;
    }
};

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> v, v2;
        v2 = nums;
        sort(v2.begin(), v2.end());
        for ( int i = 0; i<v2.size(); i++) {
            auto index = find(v2.begin(), v2.end(), nums[i]);
            
            v.push_back(index-v2.begin());
        }
        return v;
    }
};

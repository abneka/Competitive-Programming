class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) {
        vector<int> v, v2;
        v2 = nums;
        int counter = 0;
        sort(v2.begin(), v2.end());
        for ( int i=0; i< v2.size(); i++) {
            if (nums[i] == target) {
                auto index = find(v2.begin(), v2.end(), nums[i]);
                v.push_back((index-v2.begin()) +  counter);
                counter ++;
            }
        }
        return v;
    }
};

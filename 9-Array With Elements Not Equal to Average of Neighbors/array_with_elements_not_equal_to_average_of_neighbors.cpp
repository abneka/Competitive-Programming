class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> result;
        sort(nums.begin(), nums.end());
        int half = nums.size() % 2? (nums.size()/2)+1 : (nums.size()/2);
        for (int i = 0; i< half; i++) {
            result.push_back(nums[i]);
            if (half+i < nums.size()) result.push_back(nums[half +i]);
        }
        return result;
    }
};

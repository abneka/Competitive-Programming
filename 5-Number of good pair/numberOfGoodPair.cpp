class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int temp = -1, counter = 0, result = 0;
        for (int i=0; i < nums.size(); i++) {
            auto index = find(nums.begin(), nums.end(), nums[i]);
            if (temp == index-nums.begin()) {
                counter ++;
                result += counter;
                continue;
            }
            temp = index-nums.begin();
            counter = 0;
        }
        return result;
    }
};

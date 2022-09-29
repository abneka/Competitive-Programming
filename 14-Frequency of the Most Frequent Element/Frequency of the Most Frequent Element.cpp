class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        long long l = 0, r = 0;
        long long result = 0, total = 0, temp;
        while (r < nums.size()) {
            total += nums[r];
            
            while (nums[r] * ((r-l)+1) > total+k) {
                total -= nums[l];
                l++;
            }
            
            temp = result;
            result = max(temp, ((r-l)+1));
            r++;
        }
        
        return result;
    }
};

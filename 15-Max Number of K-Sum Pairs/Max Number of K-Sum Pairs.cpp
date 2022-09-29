class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        long long l = 0, r = nums.size() - 1;
        long long result = 0, total = 0;
        while (l < r) {
            total = nums[r] + nums[l];
            
            if (total == k) {
                result ++;
                l++;
                r--;
            } 
            else if (total < k) 
                l++;
            else 
                r --;
        }
        
        return result;
    }
};

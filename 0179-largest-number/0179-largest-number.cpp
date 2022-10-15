class Solution {
public:
    static bool compare (string& a, string& b) {
        return a+b>b+a;
    }
    
    string largestNumber(vector<int>& nums) {
        vector<string> str;
        for (auto num : nums) 
            str.push_back(to_string(num));
        sort(str.begin(), str.end(), compare);
        string result;
        for (auto num: str) 
            result += num;
        while (result[0] == '0' && result.length()>1) 
            result.erase(0,1);
        return result;
    }
};
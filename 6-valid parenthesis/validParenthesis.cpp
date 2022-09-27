class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for (int i =0; i< s.size(); i++) {
            if (!stack.empty()) {
                if ((stack.top() == '(' && s[i] == ')') || (stack.top() == '[' && s[i] == ']') || (stack.top() == '{' && s[i] == '}')) {
                    stack.pop();
                    continue;
                }
            }
            stack.push(s[i]);
        }
        if (stack.empty()) return true;
        return false;
    }
};

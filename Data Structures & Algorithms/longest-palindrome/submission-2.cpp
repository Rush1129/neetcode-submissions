class Solution {
public:
    int longestPalindrome(string &s) {
        int ans=0;
        bool ok=0;
        map<char,int> mp;
        for(auto &v:s)
        {
            mp[v]++;
        }
        for(auto &v:mp)
        {
            if(v.second&1)
            {
                ans+=(v.second-1);
                ok=1;
            }
            else
            {
                ans+=v.second;
            }
        }
        return ans+ok;
    }
};
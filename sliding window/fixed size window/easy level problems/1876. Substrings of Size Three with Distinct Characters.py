"""
Question:

A string is good if there are no repeated characters. 

Given a string s , return the number of good substrings of length three in s . 

Note that if there are multiple occurrences of the same substring, every occurrence should be counted. 

A substring is a contiguous sequence of characters in a string. 

  

Example 1: 

Input: s = "xyzzaz" 
Output: 1 
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".  
The only good substring of length 3 is "xyz". 
 

Example 2: 

Input: s = "aababcabc" 
Output: 4 
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc". 
The good substrings are "abc", "bca", "cab", and 

 """

# Solution: 

class Solution: 

    def countGoodSubstrings(self, s: str) -> int: 

        d  = {} 

        i=j=0 

        res = 0 

        while(j<len(s)): 

            if s[j] in d: 

                d[s[j]] +=1 

            else: 

                d[s[j]]=1 

            if j-i+1<3: 

                j+=1 

            elif j-i+1==3: 

                if len(d)==3: 

                    res +=1 

                if s[i] in d: 

                    d[s[i]] -=1 

                    if d[s[i]]==0: 

                        d.pop(s[i]) 

                i+=1 

                j+=1 

        return res 

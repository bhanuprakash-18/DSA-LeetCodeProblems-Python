"""
Question:

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order. 

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 

  

Example 1: 

Input: s = "cbaebabacd", p = "abc" 
Output: [0,6] 
Explanation: 
The substring with start index = 0 is "cba", which is an anagram of "abc". 
The substring with start index = 6 is "bac", which is an anagram of "abc". 
 

Example 2: 

Input: s = "abab", p = "ab" 
Output: [0,1,2] 
Explanation: 
The substring with start index = 0 is "ab", which is an anagram of "ab". 
The substring with start index = 1 is "ba", which is an anagram of "ab". 
The substring with start index = 2 is "ab", which is an anagram of "ab". 

"""

#  Solution: 

class Solution: 

    def findAnagrams(self, s: str, p: str) -> List[int]: 

        d={} 

        i=j=0 

        res = [] 

        for k in p: 

            if k in d: 

                d[k]+=1 

            else: 

                d[k]=1 

        count = len(d) 

        ls = len(s) 

        lp = len(p) 

        while j<ls: 

            t = s[j] 

            r = s[i] 

            if t in d: 

                d[t]-=1 

                if d[t]==0: 

                    count-=1 

            if j-i+1 < lp: 

                j+=1 

            elif j-i+1 == lp: 

                if count ==0: 

                    res.append(i) 

                if r in d: 

                    if d[r]==0: 

                        count +=1 

                    d[r]+=1 

                i+=1 

                j+=1 

        return res 

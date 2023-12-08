"""
Question:

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'. 

For example, "ACGAATTCCG" is a DNA sequence. 

When studying DNA, it is useful to identify repeated sequences within the DNA. 

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order. 

  

Example 1: 

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" 
Output: ["AAAAACCCCC","CCCCCAAAAA"] 
 

Example 2: 

Input: s = "AAAAAAAAAAAAA" 
Output: ["AAAAAAAAAA"] 

"""

#  Solution: 

class Solution: 

    def findRepeatedDnaSequences(self, s: str) -> List[str]: 

        i=j=0 

        d={} 

        c=[] 

        while j<len(s): 

            if j-i+1<10: 

                j+=1 

            if j-i+1==10: 

                t = s[i:j+1] 

                if t in d: 

                    if t not in c: 

                        c.append(s[i:j+1]) 

                else: 

                    d[t]=1 

                i+=1 

                j+=1 

        return c 

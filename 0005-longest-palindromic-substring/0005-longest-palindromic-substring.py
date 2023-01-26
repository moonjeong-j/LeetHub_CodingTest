class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i,l=0,0
        for j in range(len(s)):
            if s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
                # print(s[i: i+l])
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
                # print(s[i: i+l])
        return s[i: i+l]

"""
1. 가장 긴 substring의 시작 index를 i에, 길이는 l에 저장한다.
2. j로 s를 순회하면서 s[j-l-1:j+1], 즉 j를 기준으로 l+1만큼의 길이를 가진 (저장된 l의 길이보다 2 더 큰) substring이 palindrome인지 검사한다. 맞으면 i와 l을 update한다.
"""    
"""
정말 단순히, s의 모든 substring이 palindromic한지 검사하는 알고리즘
class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = ""
        if len(s) <= 1:
            return s
        
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(long) >= j-i:
                    continue
                elif s[i:j] == s[i:j][::-1]:
                    long = s[i:j]

        return long
"""    

        
    
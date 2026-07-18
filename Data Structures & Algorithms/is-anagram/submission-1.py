class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            lst= list(s)
            for i in t:
                try:
                    lst.remove(i)
                except:
                    return False
            return True
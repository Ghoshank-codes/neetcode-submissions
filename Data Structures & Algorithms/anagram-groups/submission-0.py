class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt={}
        for i in strs:
            dt[tuple(sorted(i))]=dt.get(tuple(sorted(i)),[])+[i]
        return [dt[i] for i in dt]
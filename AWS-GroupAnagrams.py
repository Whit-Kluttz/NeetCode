class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listSort = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            listSort[tuple(count)].append(s)
        
        print(listSort)

        return listSort.values()

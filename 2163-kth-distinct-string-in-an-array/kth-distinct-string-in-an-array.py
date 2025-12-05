class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        countMap = {}

        for s in arr:
            countMap[s] = 1 + countMap.get(s, 0)

        for s in arr:
            if countMap[s] == 1:
                k -= 1

                if k == 0:
                    return s

        return ""
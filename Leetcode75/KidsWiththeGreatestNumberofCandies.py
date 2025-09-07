class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candy = max(candies)   # compute once
        for c in candies:
            if c + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)
        return result

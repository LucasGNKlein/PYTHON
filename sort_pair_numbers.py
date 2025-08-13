from typing import List

class Solution(object):
    def solve(self,x:int,y:int)->List[int]:
        print(f"x: {x}, y: {y}")
        return [min(x,y), max(x,y)]

sol = Solution()

print(sol.solve(5,9))
print(sol.solve(7,1))

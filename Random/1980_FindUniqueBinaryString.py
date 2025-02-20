from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ["0"] * len(nums[0])
        nums = set(nums)

        def backtrack(i):
            if "".join(res) not in nums:
                return True

            for j in range(i, len(res)):
                if backtrack(j+1):
                    return True

                res[j] = "0" if res[j] == "1" else "1"

                if backtrack(j+1):
                    return True

            return False

        backtrack(0)
        return "".join(res)
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(candidate, target):
            if not candidate:
                return True if target == 0 else False
            
            for i in range(len(candidate)):                
                temp = int(candidate[:i+1])
                if target - temp >= 0 and canPartition(candidate[i+1:], target-temp):
                    return True

            return False
        
        res = 0
        for i in range(1, n+1):
            product = i * i
            if canPartition(str(product), i):
                res += product
            
        return res
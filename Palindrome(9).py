class Solution:
    def isPalindeome(self, x:int) -> bool:
        s = str(x)
        rev = s[::-1]
        if (s==rev):
            return True
        else:
            return False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ini = 0
        fi = len(s)-1
        while(ini < fi):
            while (ini < fi and not s[ini].isalnum()):
                ini += 1
            while (ini < fi and not s[fi].isalnum()):
                fi -= 1
            if(s[ini].lower() != s[fi].lower()):
                return False
            ini += 1
            fi -= 1
        return True
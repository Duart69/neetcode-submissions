class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            if(string == ""):
                res+="999"
            else:
                for i, char in enumerate(string):
                    if(i == len(string)-1):
                        code = str(ord(char)+256)
                    else:
                        code = str(ord(char))
                        if(len(code)==1):
                            code = "00"+code
                        if(len(code)==2):
                            code = "0"+code
                    res+=code
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        string = ""
        for i in range(0, len(s),3):
            char = s[i:i+3]
            code = int(char)
            if(code>256):
                if(code == 999):
                    res.append("")
                else:
                    char = chr(code-256)
                    string += char
                    res.append(string)
                    string = ""
            else:
                char = chr(code)
                string += char
        return res


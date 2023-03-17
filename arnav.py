class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.longpalyet =[]
        for i in range(0,len(s)):
            try :
                if (s[i]==s[i+1]):
                    z = True
                    try:
                        if s[i] == s[i-1]:
                            z = False
                    except:
                        pass
                else:
                    z = False
            except:
                z = False
            if z:
                y = i
                x = i+1
                while True:
                    if x < (len(s)-1):
                        x = x + 1
                    else:
                        self.longpalyet.append(s[y:x+1])
                        break
                    if y > 0 :
                        y = y - 1
                    else :
                        a = s[0:x]
                        self.longpalyet.append(a)
                        break
                    if s[x] != s[y]:
                        a = s[(y+1):x]
                        self.longpalyet.append(a)
                        break
            else:
                x = i
                y = i
                while True:
                    if x < (len(s)-1):
                        x = x + 1
                    else:
                        self.longpalyet.append(s[y:x+1])
                        break
                    if y > 0 :
                        y = y - 1
                    else :
                        a = s[0:x]
                        self.longpalyet.append(a)
                        break
                    if s[x] != s[y]:
                        a = s[(y+1):x]
                        self.longpalyet.append(a)
                        break

        return max(self.longpalyet, key = len)
if __name__ == '__main__':
    g = Solution.longestPalindrome(Solution(),input('Enter'))
    print(g)

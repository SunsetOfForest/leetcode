class Solution:
    def isValid(self, s: str) -> bool:
        mylist = []
        for char in s:
            if mylist:
                a = mylist.pop()
                if ord(char) != ord(a)+1 and ord(char) != ord(a)+2:
                    mylist.append(a)
                    mylist.append(char)
            else:
                mylist.append(char)
        return True if not mylist else False

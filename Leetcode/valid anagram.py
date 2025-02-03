class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS={} 
        countT={}
        if len(s)!=len(t):
            print("False")
        else:
            for i in s:
                if i not in countS:
                    countS[i]= 1
                else:
                    countS[i]+=1
            for i in t:
                if i not in countT:
                    countT[i]= 1
                else:
                    countT[i]+=1  
            if countS==countT:
                return True    
            else :
                return False
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        list1=list(str(n))
        result1=0
        for x in list1:
            result1+=int(x)
        sum1=result1
        result2=1
        for y in list1:
            result2*=int(y)
        prod=result2
        sum2=sum1+prod
        if n%sum2==0:
            return True
        else:
            return False
         
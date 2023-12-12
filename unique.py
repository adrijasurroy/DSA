
#
#Imagine you're in the heart of a food lover's paradise, surrounded by a delectable array of food items, each represented #by a unique character. Your mission is to create the most satisfying culinary experience by selecting as many different food items as possible while keeping your calorie count in check.
#Your goal is to discover the longest and most satisfying substring, free from repetition, as you indulge in the flavors of a grand food festival.

#

# food=['a','p','l','c','a','c']
#cal = []

# [abcdpcabgh]
# if food[i] is not cal:
    #cal[]

class Check:
    def __init__(self,count):
        self.count=1
        self.maxn = float('-inf')

    def calorie_check(self, arr,ind,ans):
        if ind == len(arr):
            self.ans = max(self.count,self.maxn)
        if arr[ind] in ans:
            self.ans = max(self.count,self.maxn)
            self.count=1
            ind = ans.index(arr[ind])+1
            calorie_check(arr,ind,[])
        else:
            self.count+=1
            ans.add(arr[ind])
            calorie_check(arr,ind+1,ans)
    

    
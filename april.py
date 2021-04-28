# Leetcode # 121 : Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        leng = len(prices)
        profit = 0
        min_price = prices[0]

        for i in range(1,leng):
            profit = max(profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return profit

# ======================================================================================

# LeetCode # 70 : Climbing Stairs

class Solution:
    def climbStairs(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n <= 2 and n >= 0:
                return n

            f = 1
            s = 2 
            c = 0 
            
            for _ in range(2, n):
                c = f + s
                f, s  = s, c
                
            return c 

class Solution:
    
    def climbStairs(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if n <= 2 and n >= 0:
            return n

        arr = [1,2]

        for i in range(2, n):
            arr.append(arr[i-1] + arr[i-2])
        
        return arr[n-1]

# ======================================================================================

# LeetCode # 448 : Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            # index = abs(nums[i]) - 1
            nums[abs(nums[i]) - 1] = - abs(nums[abs(nums[i]) - 1])

        return [i+1 for i in range(len(nums)) if nums[i] > 0]

# ======================================================================================

# LeetCode # 287 : Find the Duplicate Number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 

        s = 1
        e = len(nums)-1
        while s + 1 <= e:
            count = 0
            m = (s + e)//2
            for num in nums:
                if num <= m: 
                    count += 1        
            if count <= m:
                s = m + 1
            else:
                e = m
        return e

# ======================================================================================

# 이것이 코딩 테스트다 그리디 # 02 : 큰 수의 법칙

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0 
result += (count) * first
result += (m - count) * second

print(result)

# ======================================================================================

# 이것이 코딩 테스트다 그리디 # 03 : 숫자 카드 게임
# min() 함수

n, m = map(int, input().split())

result = 0 

for i in range(n):
    data = list(map(int, input().split()))
    min_val = min(data)
    result = max(result, min_val)

print(result)

# 2중 for문
n, m = map(int, input().split())

result = 0 

for i in range(n):
    data = list(map(int, input().split()))
    min_val = 10001
    for a in data:
        min_val = min(min_val, a)
    result = max(result, min_val)

print(result)

# ======================================================================================

# LeetCode # 1071 : Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2) && str1 == str2:
            return str1
        elif len(str1) < len(str2):
            str1, str2 = str2, str1
            return self.gcdOfStrings(str1, str2)
        elif str1[: len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return ''
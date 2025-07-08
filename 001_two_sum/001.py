'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2, 7, 11, 15], target = 9  
Output: [0, 1]  
Explanation: Because nums[0] + nums[1] == 9, return [0, 1]
'''
# 第一次作答:
'''
def two_sum(nums, target):
    for i in nums:
        for v in nums[1:]:
            if i + v == target:
            return nums[i,v]
'''
# 學了range() 和 len() 用法 , 第二次作答:
'''
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
'''
# 學習最優解 , 使用 hash map (字典) , 時間複雜度 O(n):
'''
O(n) ?
O(n) 就是說: 運算時間會隨著資料量 n 的大小「線性成長」
舉例解釋
如果有 100 個數字 , for 迴圈就跑 100 次。
如果有 10,000 個數字 , for 迴圈就跑 10,000 次。
每增加一個元素 , 就多花一點點時間

常見的複雜度 (由慢到快) :
寫法        中文說明	意思
O(1)	    常數時間	不管多少資料，處理時間都一樣快
O(log n)	對數時間	資料量變大時，處理時間增加很慢（如二分搜尋）
O(n)	    線性時間	資料量變大時，處理時間「等比例」增加
O(n^2)	    平方時間	資料量變大時，處理時間變更快變慢
'''
def two_sum(nums, target):
    lookup = {}  # 1. 建立一個空字典，叫做 lookup，用來記錄「數字：索引」
    for i, num in enumerate(nums):  # 2. 用 enumerate() 同時取得索引 i 和數值 num
        diff = target - num  # 3. 算出目前 num 要搭配什麼數才會剛好等於 target
        if diff in lookup:  # 4. 檢查這個差值 diff 是否已經出現在字典裡
            return [lookup[diff], i]  # 5. 如果有，代表找到了兩個數，回傳它們的索引
        lookup[num] = i  # 6. 如果還沒找到，就把目前這個數和索引加進字典，繼續找下一個

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9 
    print(two_sum(nums, target))

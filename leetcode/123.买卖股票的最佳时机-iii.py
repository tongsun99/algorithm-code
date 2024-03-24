#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 第二段, 从i到n-1的max_price
        max_prices = [-1] * n
        max_prices[n - 1] = prices[n - 1]
        for i in range(n - 2, -1, -1):
            max_prices[i] = max(max_prices[i + 1], prices[i])
        
        # 第一段, 最佳时机I, 0~i完成一笔交易的最大利润
        max_profits = [0] * n
        lowest = prices[0]
        for i in range(1, n):
            max_profits[i] = max(max_profits[i - 1], prices[i] - lowest)
            lowest = min(lowest, prices[i])
        
        # 合并, 枚举分界点
        res = 0
        for i in range(1, n):
            res = max(res, max_profits[i - 1] + max_prices[i] - prices[i])
            res = max(res, max_profits[i])

        return res
         
# @lc code=end

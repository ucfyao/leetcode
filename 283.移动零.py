#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 官方解法：双指针采用快速排序的思路
        # n = len(nums)

        # left = right = 0
        # while right < n:
        #     if nums[right] != 0:
        #         # 当 nums[right] 不为0时，将其值与 nums[left] 交换。
        #         # 可以优化：即便 left 和 right 指向相同的元素，也会执行交换（实际上这不会改变数组，但仍然会进行操作）。
        #         nums[left], nums[right] = nums[right], nums[left];
        #         left += 1;    
        #     right += 1;

        # 解法 2 思路：用指针保存相对位置，然后覆盖值，最后将剩余的位置补0。
        # 指向下一个非零元素应该放置的位置
        insert_pos = 0

        # 遍历数组
        for num in nums:
            if num != 0:
                # 将非零元素放到前面
                nums[insert_pos] = num
                insert_pos += 1

        # 剩下的位置补零
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1

# @lc code=end



"""Combination sum"""
class Solution:
    """class Solution"""
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        """Function combination sum"""

        all_combinations = []

        def dfs(index, current_combination, current_sum):
            """Function dfs"""
            if current_sum == target:
                all_combinations.append(current_combination)
                return

            if index >= len(candidates) or current_sum > target:
                return

            dfs(index, current_combination + [candidates[index]], current_sum + candidates[index])
            dfs(index + 1, current_combination, current_sum)

        dfs(0, [], 0)

        return all_combinations

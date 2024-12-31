class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        day_set = set(days)  # Convert list to set for faster lookup
        
        for i in range(1, last_day + 1):
            if i not in day_set:
                dp[i] = dp[i - 1]  # No need to buy a ticket if not traveling
            else:
                # Calculate costs for 1-day, 7-day, and 30-day passes
                cost1 = dp[i - 1] + costs[0]
                cost7 = dp[max(i - 7, 0)] + costs[1]
                cost30 = dp[max(i - 30, 0)] + costs[2]
                dp[i] = min(cost1, cost7, cost30)  # Take the minimum of three options
        
        return dp[-1]
        
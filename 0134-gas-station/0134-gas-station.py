class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        total_tank = 0
        current_tank = 0
        start = 0
        
        for i in range(n):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]
            
            # If current tank is negative, reset start point
            if current_tank < 0:
                start = i + 1
                current_tank = 0
        
        # If total gas is greater than or equal to total cost, return start, otherwise -1
        return start if total_tank >= 0 else -1
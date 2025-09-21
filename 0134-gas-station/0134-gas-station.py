class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start_index = 0
        total_gas = 0
        total_cost = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start_index = i+1

        return -1 if total_gas < total_cost else start_index

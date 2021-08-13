class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        trips = 0
        while trips < length:
            tank_gas = 0
            gas1 = gas[trips:]+ gas[:trips]
            cost1 = cost[trips:]+ cost[:trips]
            for i in range(length):
                tank_gas = tank_gas + gas1[i] - cost1[i]
                if tank_gas < 0:
                    break
        
            if tank_gas >= 0:
                return trips
            trips+=1
        return -1
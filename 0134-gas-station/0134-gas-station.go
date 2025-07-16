func canCompleteCircuit(gas []int, cost []int) int {
    tank, ind, tot_cost, tot_gas := 0,0,0,0
    for i := range(gas){
        tot_gas += gas[i]
        tot_cost += cost[i]
        tank += gas[i] - cost[i]
        if tank < 0{
            tank = 0
            ind = i+1
        }
    }
    if tot_gas < tot_cost{
        return -1
    }else{
        return ind
    }


}
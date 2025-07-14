func maxProfit(prices []int) int {
    diff := 0
    i := 1
    cheap := prices[0]
    for i<len(prices){
        cheap = min(cheap,prices[i])
        diff = max(diff, (prices[i] - cheap))
        i++
    }
    return diff
}
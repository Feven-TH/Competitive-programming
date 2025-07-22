func maximumUniqueSubarray(nums []int) int {
    maxx, curr, left:= 0,0,0
    set := make(map[int]int)
    for _,num := range nums{
        for set[num] != 0{
            set[nums[left]] -= 1
            curr -= nums[left]
            left += 1   
        }
        curr += num
        set[num] += 1
        maxx = max(maxx,curr)
    }
    return maxx
}
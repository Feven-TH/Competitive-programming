func intersection(nums1 []int, nums2 []int) []int {
    set := make(map[int]bool)
    for _,val := range(nums1){
        set[val] = true
    }
    res := []int{}
    for _,num := range(nums2){
        if set[num]{
            set[num] = false
            res = append(res,num)
        }
    }
    return res   
}
func countHillValley(nums []int) int {
    count := 0
    arr :=  []int{nums[0]}
    for i := 1; i < len(nums); i++{
        if nums[i] != nums[i-1]{
            arr = append(arr,nums[i])
        }
    }
    for i := 1; i < len(arr)-1; i++{
        if (arr[i]< arr[i+1] && arr[i]<arr[i-1]) || (arr[i]> arr[i+1] && arr[i]>arr[i-1]){
            count ++
        }
    }
    return count
}
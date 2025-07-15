func numJewelsInStones(jewels string, stones string) int {
    counts := 0
    set := make(map[rune]bool)
    for _,ch := range(jewels){
        set[ch] = true
    }
    for _,s := range(stones){
        if set[s] == true{
            counts++
        }
    }
    return counts
}
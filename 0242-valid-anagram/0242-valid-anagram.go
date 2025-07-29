func isAnagram(s string, t string) bool {
    if len(s) != len(t){
        return false
    }
    map_s := make(map[rune]int)
    map_T := make(map[rune]int)
    
    for _,ch := range s{
        map_s[ch]++
    }

    for _,ch := range t{
        map_T[ch]++
    }
    for k, v := range map_s{
        if map_T[k] != v{
            return false
        }
    }
    return true 
}
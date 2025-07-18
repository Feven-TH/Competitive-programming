func isIsomorphic(s string, t string) bool {
    if len(s) != len(t){
        return false
    }
    sMap := make(map[byte][]int)
    tMap := make(map[byte][]int)
    for i := range(s){
        sMap[s[i]] = append(sMap[s[i]], i)
        tMap[t[i]] = append(tMap[t[i]], i) 
    }
    for i := range(s){
        if !equal(sMap[s[i]], tMap[t[i]]){
            return false
        }
    }
    return true
}
func equal(a, b[]int) bool{
    if len(a) != len(b) {
        return false
    }
    for i := range a{
        if a[i] != b[i] {
            return false
        }
    }
    return true
}

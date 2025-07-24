func titleToNumber(columnTitle string) int {
    res := 0
    for _, char := range columnTitle{
        res = res*26 + (int(char-'A') + 1)
    }
    return res
}

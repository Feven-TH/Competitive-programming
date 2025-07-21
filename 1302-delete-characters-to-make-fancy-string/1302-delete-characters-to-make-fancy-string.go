func makeFancyString(s string) string {
    var builder strings.Builder
    rune := []rune(s)
    builder.WriteRune(rune[0])
    temp := 1
    for i := 1; i < len(s); i++{
        if rune[i] == rune[i-1]{
            temp ++
        }else{
            temp = 1
        }
        if temp < 3{
            builder.WriteRune(rune[i])
        }
        
    }
    return builder.String()
}
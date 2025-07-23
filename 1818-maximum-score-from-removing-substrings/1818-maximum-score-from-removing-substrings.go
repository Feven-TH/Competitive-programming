func maximumGain(s string, x int, y int) int {
    stack := []rune{}
    res := 0
    var high rune
    var low rune
    var expensive int
    var cheap int
    if x > y{
        high = 'a'
        low = 'b'
        expensive = x
        cheap = y
    }else{
        high = 'b'
        low = 'a'
        expensive = y
        cheap = x
    }

    for _,ch := range s{
        if ch == low && len(stack)>0 && stack[len(stack)-1] == high{
            stack = stack[:len(stack)-1]
            res += expensive
        }else{
            stack = append(stack, ch)
        }
    }
    final_stack := []rune{}
    for _,ch := range stack{     
        if ch == high && len(final_stack) > 0 && final_stack[len(final_stack)-1] == low{   
            final_stack = final_stack[:len(final_stack)-1]    
            res += cheap
        }else{
            final_stack = append(final_stack, ch)
        }
    } 
    
    return res
}
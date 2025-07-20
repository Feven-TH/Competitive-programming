func reverse(x int) int {
    r := 0 
    max := int(math.Pow(2, 31) - 1)
    min := -int(math.Pow(2, 31))
    for x != 0{
        temp := x % 10
        x /= 10
        if r > max/10 || (r == max/10 && temp > 7) {
            return 0
        }
        if r < min/10 || (r == min/10 && temp < -8) {
            return 0
        }
        r = r*10 + temp
    }
    return r
    }

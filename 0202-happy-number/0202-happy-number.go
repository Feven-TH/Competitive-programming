func isHappy(n int) bool {
    set := make(map[int]bool)
    for n != 1 && !set[n] {
        set[n] = true           
        sum := 0
        temp := n
        for temp > 0 {
            d := temp % 10
            sum += d *d
            temp /= 10
        }
        n = sum             
    }
    return n == 1
}
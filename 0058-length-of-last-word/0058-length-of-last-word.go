func lengthOfLastWord(s string) int {
    s = strings.TrimSpace(s)
	if len(s) == 0 {
		return 0
	}
	ind := strings.LastIndex(s, " ")
	if ind == -1 {
		return len(s)
	}
	return len(s) - (ind + 1)
}


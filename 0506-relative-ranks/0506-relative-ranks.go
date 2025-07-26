func findRelativeRanks(score []int) []string {
	n := len(score)
	idx := make([]int, n)
	for i := 0; i < n; i++{
		idx[i] = i
	}

	sort.Slice(idx, func(i, j int) bool {
		return score[idx[i]] > score[idx[j]]
	})

	ans := make([]string, n)

	for i := 0; i < n; i++ {
		org := idx[i]
		rank := i + 1

		switch rank {
		case 1:
			ans[org] = "Gold Medal"
		case 2:
			ans[org] = "Silver Medal"
		case 3:
			ans[org] = "Bronze Medal"
		default:
			ans[org] = strconv.Itoa(rank)
		}
	}

	return ans
}
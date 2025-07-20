func sortSentence(s string) string {
  words := strings.Split(s, " ")
    sort.Slice(words, func(i, j int) bool {
        return words[i][len(words[i])-1] < words[j][len(words[j])-1]
    })
    for i := range words {
        words[i] = words[i][:len(words[i])-1]
    }
    return strings.Join(words, " ")
}

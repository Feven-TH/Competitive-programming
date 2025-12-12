class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]),x[0] != "OFFLINE"))
        mentions = [0]* numberOfUsers
        offline = [0]* numberOfUsers
        for m,T,u in events:
            t = int(T)
            # print(m,int(t),u)
            if m == "OFFLINE":
                offline[int(u)] = t + 60
            else:
                if u == "HERE":
                    for i in range(len(mentions)):
                        if offline[i] == 0 or t >= offline[i]:
                            mentions[i] += 1
                elif u == "ALL":
                    for i in range(len(mentions)):
                        mentions[i] += 1
                else:
                    for i in u.split(" "):
                        ind = int(i[2:])
                        mentions[ind] += 1
        return mentions
                        



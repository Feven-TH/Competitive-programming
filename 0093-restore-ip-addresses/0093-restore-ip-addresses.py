class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = [] 
        path = []

        def bt(start):
            # base
            if len(path) == 4:
                if start == len(s):
                    ans.append(".".join(path))
                return

            for end in range(start, len(s)):
                cur_slice = s[start:end+1]
                if len(cur_slice) > 1 and cur_slice[0] == "0":
                    break
                
                if int(cur_slice) > 255:
                    break
                
                path.append(cur_slice)
                bt(end + 1)
                path.pop()
 
        if not 4 <= len(s) <= 12:
            return []

        bt(0)
        return ans
        
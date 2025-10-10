class Solution:
    def minMaxDifference(self, num: int) -> int:
        n = str(num)
        r = ""
        for i in n:
            if i != '9':
                r = i
                break
        if r:
            maxx = n.replace(r,'9')
        else:
            maxx = n
        minn = n.replace(n[0],'0')

        return int(maxx) - int(minn)
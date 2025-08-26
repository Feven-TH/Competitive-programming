class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        areaMaxx = 0
        diagMaxx = 0

        for l,w in dimensions:
            diag = l**2 + w**2
            area = l*w
            if diag > diagMaxx:
                diagMaxx = diag
                areaMaxx = area
            elif diag == diagMaxx:
                areaMaxx = max(areaMaxx, area)
        return areaMaxx

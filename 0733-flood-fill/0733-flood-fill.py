class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(-1,0), (0,-1), (0 ,1), (1,0)]
        q = deque([(sr,sc)])
        og = image[sr][sc]

        if image[sr][sc] == color:
            return image
        
        while q:
            i ,j = q.popleft()
            image[i][j] = color  

            for dr , dc in directions:
                row = dr + i
                col = dc + j

                if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == og:
                    q.append((row,col))   
                    
        return image
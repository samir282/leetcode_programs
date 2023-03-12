class Solution:
    def colored_image(image: List[List[int]], sr:int, sc: int, color: int, value: int) -> List[List[int]]:
        if sr<0 or sc<0 or sr>= len(image) or sc>= len(image[0]):
            return image
        if image[sr][sc]==color:
            return image
        if image[sr][sc]==value:
            image[sr][sc] = color
            image = Solution.colored_image(image, sr+1, sc, color, value)
            image = Solution.colored_image(image, sr-1, sc, color, value)
            image = Solution.colored_image(image, sr, sc+1, color, value)
            image= Solution.colored_image(image, sr, sc-1, color, value)
        return image
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        value = image[sr][sc]
        image = Solution.colored_image(image, sr, sc, color, value)
        return image

        
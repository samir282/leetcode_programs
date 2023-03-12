class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        for rec in rectangles:
            small = min(rec)
            rec[:] = [small] * len(rec)
            print(rec)
        large = max(rectangles)
        print(large)
        return 0
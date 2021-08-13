class Solution:
    def maximumUnits(self, boxes: List[List[int]], truck: int) -> int:
        boxes = sorted(boxes, key = lambda x: x[1], reverse = True)
        count = 0
        for a,b in boxes:
            if truck - a >= 0:
                count = count + a*b
                truck -= a
            else:
                count = count + truck * b 
                break
        return count
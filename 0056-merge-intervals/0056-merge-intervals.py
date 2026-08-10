class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = list()
        #SORTING THE Start TO AVOID STORE TUPLE and check for the range
        intervals = sorted(intervals, key=lambda x: x[0])
        n = len(intervals)
        # NOW Start s & end e if next range lie between update s&e else change the s&e
        s,e = intervals[0][0],intervals[0][1]
        for pos in range(1,n):
            if s<=intervals[pos][0]<=e:
                s,e = min(s,intervals[pos][0]),max(e,intervals[pos][1])
            else:
                result.append([s,e])
                s,e = intervals[pos]
        result.append([s,e])
        return result
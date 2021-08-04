class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr1 = []
        arr2 = []
        for i in range(len(intervals)):
            arr1.append(intervals[i][0])
            arr2.append(intervals[i][1])
        arr = []
        begining = intervals[0][0]
        deadline = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] == begining:
                deadline = max(deadline, intervals[i][1])
                continue
            if intervals[i][0] > deadline:
                temp = []
                temp.append(begining)
                temp.append(deadline)
                arr.append(temp)
                begining = intervals[i][0]
                deadline = intervals[i][1]
            else:
                deadline = max(deadline, intervals[i][1])
        temp = []
        temp.append(begining)
        temp.append(deadline)
        arr.append(temp)
        return arr

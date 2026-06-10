class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandcount = [students.count(0), students.count(1)]
        for i in sandwiches:
            print(sandcount)
            if sandcount[i] > 0:
                sandcount[i] -= 1
            else:
                return sum(sandcount)
        return 0


import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        def improvement(pass_students, total_students):
            return (pass_students + 1) / (total_students + 1) - pass_students / total_students
        heap = []
        for pass_students, total_students in classes:
            heapq.heappush(heap, (-improvement(float(pass_students), float(total_students)), float(pass_students), float(total_students)))
        for _ in range(extraStudents):
            imp, pass_students, total_students = heapq.heappop(heap)
            pass_students += 1
            total_students += 1
            heapq.heappush(heap, (-improvement(pass_students, total_students), pass_students, total_students))
        total_ratio = 0
        for _, pass_students, total_students in heap:
            total_ratio += float(pass_students) / float(total_students)
        return total_ratio / float(len(classes))
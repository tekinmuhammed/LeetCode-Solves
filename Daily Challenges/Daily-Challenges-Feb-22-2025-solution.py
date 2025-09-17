# 📅 LeetCode 729 - My Calendar I

# **Difficulty:** Medium  
# **Problem Link:** [LeetCode 729](https://leetcode.com/problems/my-calendar-i)

# 🧠 Problem Description
# [Github LeetCode 729 - My Calendar I](https://github.com/tekinmuhammed/LeetCode-Solves/tree/main/Medium/729.%20My%20Calendar%20I)

class MyCalendar(object):

    def __init__(self):
        self.bookings = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        for s, e in self.bookings:
            if max(s, startTime) < min(e, endTime):
                return False
        self.bookings.append((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
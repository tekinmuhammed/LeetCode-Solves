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
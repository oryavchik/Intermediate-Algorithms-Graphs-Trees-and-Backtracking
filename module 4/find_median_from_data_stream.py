"""Find Median from Data Stream"""

import heapq

class MedianFinder:
    """class MedianFinder"""
    def __init__(self):
        """Function init"""
        self.lefthalf = []
        self.righthalf = []

    def add_num(self, num: int) -> None:
        """Function adds number"""
        if not self.lefthalf or num <= -self.lefthalf[0]:
            heapq.heappush(self.lefthalf, -num)
        else:
            heapq.heappush(self.righthalf, num)

        if len(self.lefthalf) > len(self.righthalf) + 1:
            heapq.heappush(self.righthalf, -heapq.heappop(self.lefthalf))

        elif len(self.righthalf) > len(self.lefthalf):
            heapq.heappush(self.lefthalf, -heapq.heappop(self.righthalf))

    def find_median(self) -> float:
        """Function finds median"""
        if len(self.lefthalf) > len(self.righthalf):
            return -self.lefthalf[0]

        if len(self.righthalf) > len(self.lefthalf):
            return self.righthalf[0]

        return (-self.lefthalf[0] + self.righthalf[0]) / 2.0

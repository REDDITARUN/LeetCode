from collections import deque
class MyStack(object):

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque() 
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.queue1:
            self.queue2.append(self.queue1.popleft())

        self.queue1.append(x)

        while self.queue2:
            self.queue1.append(self.queue2.popleft())
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue1.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
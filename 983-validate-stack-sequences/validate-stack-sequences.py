class Solution(object):
    def validateStackSequences(self, pushed, popped):
        # create an empty stack
        stack = []
        # now pointer for popped
        pop_pt = 0

        # now simulate the insertion and deletion
        for val in pushed:
            stack.append(val)

            while stack and stack[-1] == popped[pop_pt]:
                stack.pop()
                pop_pt += 1

        if pop_pt == len(popped):
            return True
        else:
            return False
        
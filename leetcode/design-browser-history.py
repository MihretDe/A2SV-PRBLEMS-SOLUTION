class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.previous = None
class BrowserHistory:

    def __init__(self, homepage: str):
        new_node = ListNode(homepage)
        self.head = new_node
        self.curr= new_node

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        
        # if self.curr.next.previous:
        #     self.curr.next.previous =None
        # self.curr.next = None
        self.curr.next = new_node
        new_node.previous = self.curr
        self.curr=new_node

        

    def back(self, steps: int) -> str:
        temp = self.curr
        while temp.previous and steps:
            temp = temp.previous
            steps-=1
        self.curr=temp
        return temp.val

        

    def forward(self, steps: int) -> str:
        temp = self.curr
        while temp.next and steps:
            temp = temp.next
            steps-=1
        self.curr=temp
        return temp.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
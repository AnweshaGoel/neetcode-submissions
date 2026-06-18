class page:
    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = page(homepage)
        self.curr = self.home

    def visit(self, url: str) -> None:
        new = page(url)
        self.curr.next = new
        new.prev = self.curr
        self.curr = new

    def back(self, steps: int) -> str:
        i = 0
        while self.curr.prev and i < steps:
            self.curr = self.curr.prev
            i += 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        i = 0
        while self.curr.next and i < steps:
            self.curr = self.curr.next
            i += 1
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
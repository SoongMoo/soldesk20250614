a = 10
PI = 3.141592
def f(x):
    return 3*x + 5
class Calculator: 
    # 생성자
    def __init__(self, first, second): # setData()는 멤버필드를 초기화 하기 위해서
        self.first = first
        self.second = second
    def add(self):
        self.result = self.first + self.second
    def div(self):
        self.result = self.first / self.second
		
b = Calculator(10, 5)
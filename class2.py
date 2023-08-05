class Hello():
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print(self.name + "안녕하세요")
    def goodbye(self):
        print("안녕히 가세요")

a = Hello('홍길동')
a.greeting()
b = Hello("이길동")
c = Hello("박길동")
c.greeting()
a.goodbye()
b.goodbye()
class God():
    def __init__(self, name, age, country, height):
        self.name = name
        self.age = age
        self.country = country
        self.height = height
    def introduce(self):
        print(f"나의 이름은 {self.name}이고, 나이는 {self.age}, 키는 {self.height}이며, {self.country}에서 태어났습니다")
    
a = God("이서준", 127, "중국", 135)
b = God("박성현", 12, "대한민국", 136)
c = God("홍길동", 25, "영국", 185)
d = God("티라노", 66000000, "백악기", 1200)
e = God("공명 필", 26, "대한민국", 176)

a.introduce()
b.introduce()
c.introduce()
d.introduce()
e.introduce()
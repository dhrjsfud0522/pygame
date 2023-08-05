class Fighter(object):
    def __init__(self, model, missile):
        self.model = model
        self.missile = missile
    def attack(self):
        print(self.model + " 출격!")
    def fire(self):
        print(self.missile + " 발사!")

fighter1 = Fighter("이서준", "입냄새")
fighter1.attack()
fighter1.fire()
fighter2 = Fighter("박성현", "컴퓨터 끄기")
fighter2.attack()
fighter2.fire()


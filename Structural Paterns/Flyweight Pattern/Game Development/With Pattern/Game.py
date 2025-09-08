from Bullet import Bullet

class Game:
    def main(self):
        bullet1 = Bullet("red", 3, 7, 40)
        bullet1.render()
        bullet1.move(10, 10)
        bullet1.render()

        bullet2 = Bullet("green", 6, 6, 30)
        bullet2.render()

        bullet3 = Bullet("red", 4, 4, 30)
        bullet3.render()

if __name__ == "__main__":
    game = Game()
    game.main()
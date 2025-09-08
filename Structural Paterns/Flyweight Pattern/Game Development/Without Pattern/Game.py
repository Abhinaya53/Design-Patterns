from Bullet import Bullet

class Game:
    def main(self):
        bullet = Bullet("red", 3, 7, 40)
        bullet.render()
        bullet.move(10, 10)
        bullet.render()

if __name__ == "__main__":
    game = Game()
    game.main()
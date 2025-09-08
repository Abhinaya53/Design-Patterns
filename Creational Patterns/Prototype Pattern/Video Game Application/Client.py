from Warrior import Warrior
from Archer import Archer
from Mage import Mage

warrior1 = Warrior("Conan", 150, 30, 20)
archer1 = Archer("Legolas", 100, 25, 15)
mage1 = Mage("Gandalf", 80, 40, 10)

print("Original Characters:")
warrior1.display_character()
archer1.display_character()
mage1.display_character()

warrior2 = warrior1.clone()
archer2 = archer1.clone()
mage2 = mage1.clone()

print("\n\nCloned Characters:")
warrior2.display_character()
archer2.display_character()
mage2.display_character()
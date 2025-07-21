from guerrier import Guerrier
from magicien import Magicien

if __name__ == "__main__":
    guerrier = Guerrier()
    magicien = Magicien()

    magicien.set_name("Laurant")
    guerrier.set_name("Alex")

    print(f"Guerrier: {guerrier.get_name()} \nvie: {guerrier.get_vie()}")
    print(f"Magicie: {magicien.get_name()} \nvie: {magicien.get_vie()}")

    guerrier.attaque(magicien)
    magicien.lancer_sort(guerrier)

    print(f"Guerrier: {guerrier.get_name()} \nvie: {guerrier.get_vie()}")
    print(f"Magicie: {magicien.get_name()} \nvie: {magicien.get_vie()} ")

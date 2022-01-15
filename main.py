# belajar OOP

class Hero :
    __jumlah = 0

    # encapsulasi : membuat semua variable menjadi private supaya nantinya menggunakan getter dan setter
    def __init__(self, nama, health, attack, armor) :
        self.__nama = nama
        self.__health = health
        self.__attack = attack
        self.__armor = armor 
        Hero.__jumlah += 1
  

class Warrior(Hero) : # inherintance
    pass

class Mage(Hero) :
    pass

eudora = Hero("eudora", 100, 7, 3)
zilong = Warrior("zilong", 100, 8.5 , 7)
miya = Mage("miya",100, 6.8, 6)

print(eudora.__dict__)



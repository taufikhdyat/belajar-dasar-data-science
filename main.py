# belajar OOP

class Hero :
    __jumlah = 0

    # encapsulasi : membuat semua variable menjadi private supaya nantinya menggunakan getter dan setter
    # getter dan setter diperlukan supaya atribut dapat diakses
    def __init__(self, name, health, attack, armor) :
        self.__name = name
        self.__health = health
        self.__attack = attack
        self.__armor = armor 
        self.info = "name : {}  \n\t health : {}".format(self.__name,self.__health)
        Hero.__jumlah += 1

    
        
    #method static (decorator)
    @staticmethod # tidak mengambil argumen
    def getJumlah() : 
        return Hero.__jumlah

    @classmethod  # mengambil argumen
    def getJumlah1(self):
        return self.__jumlah


# inherintance
class Warrior(Hero) : 
    pass

class Mage(Hero) :
    pass

eudora = Hero("eudora", 100, 7, 3)
zilong = Warrior("zilong", 100, 8.5 , 7)
miya = Mage("miya",100, 6.8, 6)

#print(miya.__name) # ini akan error, karena atributnya private
print(zilong.info)
#test jumlah
print(Hero.getJumlah())

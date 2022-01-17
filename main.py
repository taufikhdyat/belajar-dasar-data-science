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
        #self.info = "name : {}  \n\t health : {}".format(self.__name,self.__health) ... kalo gini bisa dirubah user
        #self.__info = "name : {}  \n\t health : {}".format(self.__name,self.__health) ... kalo gini bisa kita akses
        #solusinya liat property
        Hero.__jumlah += 1

    @property #mengubah method menjadi seperti variable
    def info(self):
        return "name : {}  \n\t health : {}".format(self.__name, self.__health)

   
    #method static (decorator)
    @staticmethod # tidak mengambil argumen
    def getJumlah() : 
        return Hero.__jumlah

    @classmethod  # mengambil argumen
    def getJumlah1(self):
        return self.__jumlah


# inherintance
class Hero_Intelligent(Hero) : 
    pass

class Hero_Strength(Hero) :
    pass

snipper = Hero_Intelligent("snippper", 100, 6, 6)
earthshaker = Hero_Strength("earthshaker", 100, 8.5, 5)

print(earthshaker.info)




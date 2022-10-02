"""
# paradigma programming 
structural => procedural
 object oriented programming

bedanya
- procedural akan dieksekusi berdasarkan urutan

- object oriented menganggap semua adalah object


class => memiliki atribut dan method

class hero :
	atribut => nama, power, defense
	method => menyerang, bertahan, begerak


"""


# deklarasi class

class Hero:
	pass


hero1=Hero() # object / instance (instansiate)
hero2 = Hero()
hero3= Hero()

hero1.name="sniper"
hero1.health=100

hero2.name="sven"
hero2.health=200

hero3.name="ucup"
hero3.health=1000


print(hero1)
print(hero1.__dict__)
print(hero1.name)



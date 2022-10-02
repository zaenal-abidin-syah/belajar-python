"""
__init___

"""


# class Hero:
# 	def __init__(self,name,health, power, armor):
# 		self.name = name
# 		self.health = health
# 		self.power = power
# 		self.armor = armor

# hero1 = Hero("sniper", 100, 12, 30)
# print(hero1.__dict__)
# print(hero1.name)


"""
class dan instance variable

"""

# print(Hero.__dict__) #tidak ada variable name health dll

# variable static adalah variable yang ada di dalam class itu sendiri / biasa disebut class variable



class Hero:
	# class variable
	jumlah = 0
	def __init__(self,name,health, power, armor):
		# instance variable
		self.name = name
		self.health = health
		self.power = power
		self.armor = armor
		Hero.jumlah+=1
	# method tanpa return / void
	def siapa(self):
		print("namaku adalah "+self.name)
	# method dengan argument
	def healthUp(self, up):
		self.health += up
	# method dengan return
	def getHealth(self):
		return self.health


hero1 = Hero("sniper", 100, 12, 30)
print(hero1.__dict__)
# print(Hero.jumlah)
# hero1.siapa()

hero1.healthUp(10)
print(hero1.__dict__)

print(hero1.getHealth())
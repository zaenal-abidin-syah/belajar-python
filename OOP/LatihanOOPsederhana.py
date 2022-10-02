class Hero(object):
 	"""docstring for Hero"""
 	jumlah = 0
 	def __init__(self,name,health, power, armor):
 		# instance variable
 		self.name = name
 		self.health = health
 		self.power = power
 		self.armor = armor
 		Hero.jumlah+=1
 	def serang(self, lawan):
 		print(f"{self.name} menyerang {lawan.name}")
 		lawan.diserang(self, self.power)
 	def diserang(self, lawan, power_lawan):
 		print(f"{self.name} diserang {lawan.name}")
 		attact_diterima = power_lawan/self.armor
 		print("serangan terasa "+ str(attact_diterima))
 		self.health -= attact_diterima
 		print(f"darah {self.name} tersisa {self.health}")



sniper = Hero("sniper", 100, 10, 5)
rikimaru = Hero("rikimaru", 100, 20, 10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)

# ada class variable
# ada instance variable / publik variable

# private variable
# variable yang ada namun tidak bisa diakses
# misalkan ada sebuah object tombol
# variable yang dapat kita akses seperti color, background color dll adalah publik variable yang dapat kita akses atau kita ubah
# selain itu ada juga misalnya seperti font, border radius dst yang tidak dapat diakses atau merupakan private variable


# tujuannya adalah variable yang menempel pada object tidak terlalu banyak




# membuat variable privat


class Hero:
	jumlah = 0
	__privateJumlah = 0

	def __init__(self, name, health):
		self.name = name
		self.health = health

		# membuat variable instance private
		self.__private = "private"

		# variable instance protected
		self._protected = "protected"

lina = Hero("lina", 100)
# print(lina.__dict__)
# print(lina.health)
# print(lina.__private) # tidak bisa
# print(lina.__dict__)
# print(lina._protected)
# lina._protected = "testing"
# print(lina.__dict__)
# print(lina._protected)


# print(Hero.__privateJumlah) # tidak bisa








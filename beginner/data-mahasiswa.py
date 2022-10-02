import os


def menambahDataMahasiswa():
	print("tambahkan data mahasiswa : ")
	nama = input("masukan nama mahasiswa \t:")
	nim = input("masukan nim mahasiswa \t:")
	email = input("masukan email mahasiswa \t:")
	return {
		"nama":nama,
		"nim":nim,
		"email":email
	}



dataMhs = []

while True:
	os.system("clear")
	print(f"""
		data-mahasiswa :
		{dataMhs}
		""")
	tanya = input("apakah anda ingin menambahkan data mahasiswa tekan ENTER untuk melanjutkan : ")
	if not tanya:
		mhs = menambahDataMahasiswa()
		dataMhs.append(mhs)
	elif tanya == "no":
		break
	else:
		print("tekan ENTER untuk melanjutkan / ketikan n untuk berhenti")
		break

		
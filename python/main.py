import cv2
import random
import os

def tambahkan_teks_pada_foto(input_path, output_path, teks, posisi=(10, 30), font_scale=1.2, font_thickness=2, font_color=(255, 255, 255)):
    # Baca foto
    # foto = cv2.imread(input_path)
    
    # # Tambahkan teks
    # cv2.putText(foto, teks, posisi, cv2.FONT_HDFONT_HERSHEY_SIMPLEX, font_scale, font_color, font_thickness)
    
    # # Simpan foto yang sudah diedit
    # cv2.imwrite(output_path, foto)
    # Baca foto
    desa = 'Napis'
    kec = 'Kecamatan Tambakrejo'
    kab = 'Kabupaten Bojonegoro'
    prov = 'Jawa Timur'
    foto = cv2.imread(input_path)
    tinggi, lebar, _ = foto.shape
    
    # Tentukan ukuran teks
    teks_lebar , teks_tinggi = cv2.getTextSize(teks, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]
    teks_lebar_desa , teks_tinggi_desa = cv2.getTextSize(desa, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]
    teks_lebar_kec , teks_tinggi_kec = cv2.getTextSize(kec, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]
    teks_lebar_kab , teks_tinggi_kab = cv2.getTextSize(kab, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]
    teks_lebar_prov , teks_tinggi_prov = cv2.getTextSize(prov, cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_thickness)[0]
    # teks_lebar = lebar // 3
     
    # Hitung posisi teks di pojok kanan atas
    posisi_x = lebar - teks_lebar - 10  # 10 adalah jarak dari tepi
    posisi_y = teks_tinggi + 10         # 10 adalah jarak dari tepi

    teks_desa_x = (lebar - teks_lebar_desa) - 10
    teks_desa_y = posisi_y + teks_tinggi_desa + 15  # Jarak vertikal tetap 10 piksel dari atas
    teks_kec_x = (lebar - teks_lebar_kec) - 10
    teks_kec_y = teks_desa_y + teks_tinggi_kec + 15
    teks_kab_x = (lebar - teks_lebar_kab) - 10
    teks_kab_y = teks_kec_y + teks_tinggi_kab + 15
    teks_prov_x = (lebar - teks_lebar_prov) - 10
    teks_prov_y = teks_kab_y + teks_tinggi_prov + 15
    
    # Tambahkan teks
    cv2.putText(foto, teks, (posisi_x, posisi_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, font_thickness)
    cv2.putText(foto, desa, (teks_desa_x, teks_desa_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, font_thickness)
    cv2.putText(foto, kec, (teks_kec_x, teks_kec_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, font_thickness)
    cv2.putText(foto, kab, (teks_kab_x, teks_kab_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, font_thickness)
    cv2.putText(foto, prov, (teks_prov_x, teks_prov_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, font_color, font_thickness)
    
    # Simpan foto yang sudah diedit
    cv2.imwrite(output_path, foto)

folder_path = './all'

# Buat list untuk menyimpan nama file
nama_file = []

# Loop melalui setiap file dalam folder
for file in os.listdir(folder_path):
    # Cek apakah file merupakan file (bukan folder)
    if os.path.isfile(os.path.join(folder_path, file)):
        # Tambahkan nama file ke dalam list
        nama_file.append(file)


# Print list nama file
# print(nama_file)

# Contoh penggunaan
output_folder = 'result/'
teks = '10 Feb 2024'

jam = 15
menit = 1
print("Progress : ", end='')
for file in nama_file:
    # print('menit ke', menit)
    input_path = folder_path + '/' +file
    output_path = output_folder + '/' + file
    teks_result = teks + f' {jam}.' + '{:02d}'.format(menit) + '.{:02d}'.format(random.randint(1, 59))
    tambahkan_teks_pada_foto(input_path, output_path, teks_result)
    menit += 3
    if menit == 58:
        menit = 1
        jam += 1
    print('', end='#')

print('selesai!')

# input_folder = 


# for i in range(1, 13):  # Misalnya, ada 10 foto dalam folder
#     input_path = input_folder + f'{i}.jpg'
#     output_path = output_folder + f'{i}_dengan_teks.jpg'
#     teks_result = teks + f''
#     tambahkan_teks_pada_foto(input_path, output_path, teks_result)

# print("Selesai!")

# NAMA  : AFFAN AKHTAR HAKEEM
# NIM   : 222410102011

import os
os.system("cls")

print("Pilih jenis sapi : ")
print("""
[1] Sapi Warrior    = 690 hari
[2] Sapi Mage       = 420 hari
[3] Sapi Assasin    = 530 hari
[4] Sapi Nolep      = 330 hari
""")
s1 = 690
s2 = 420
s3 = 530
s4 = 330
list = []

umur = int(input("Berapa total sapi yang ingin kamu jumlah umurnya? "))

for i in range (umur) :
    kode = int(input("Masukkan kode sapi ke : "))
    if kode == 1 :
        list.append(s1)
    elif kode == 2 :
        list.append(s2)
    elif kode == 3 :
        list.append(s3)
    elif kode == 4 :
        list.append(s4)
total = sum(list)

tahun = int(total / 365)
bulan = int((total - (tahun * 365)) / 30)
hari = int(total - (tahun * 365) - (bulan * 30))

print(f"\nTotal umur sapi adalah {tahun} tahun, {bulan} bulan, {hari} hari")
print("="*70)
print(f"|{'SELAMAT DATANG DI SISTEM PEMESANAN TIKET PESAWAT':^68}|")
print("-"*70)

#tampilan 1
print("="*40)
print(f"|{'Data pemesan':^38}|")
print("="*40)
nama=input(" Nama  : ")
umur=int(input(" Umur  : "))
jenis_kelamin=input(" Jenis kelamin (P/L) : ")
print("="*40)

#tampilan 2
print("="*40)
print(f"|{'Kode maskapai yang tersedia':^38}| ")
print("="*40)
print(" 3012 -> Padang - Jakarta")
print(" 4015 -> Padang - Batam")
print(" 4050 -> Padang - Bandung")
print("="*40)
	
maskapai={
3012 : ("Padang - Jakarta", 800000, 850000, 900000),
4015 : ("Padang - Batam", 500000 ,550000, 700000),
4050 : ("Padang - Bandung", 700000, 750000, 850000)}

kode_maskapai=int(input("Kode maskapai yang dipilih : "))
if kode_maskapai==3012:
	tujuan, kelas_ekonomi,kelas_bisnis,kelas_first = maskapai [3012]
elif kode_maskapai==4015:
	tujuan, kelas_ekonomi,kelas_bisnis,kelas_first = maskapai [4015]
elif kode_maskapai==4050:
	tujuan, kelas_ekonomi,kelas_bisnis,kelas_first = maskapai [4050]
else:
	print("Kode maskapai tidak valid")
#tampilan 3
print("="*40)
print(f"|{'Jenis kelas yang tersedia':^38}|")
print("="*40)
print(f" 1. Ekonomi - Rp {kelas_ekonomi}")
print(f" 2. Bisnis - Rp {kelas_bisnis}")
print(f" 3. First - Rp {kelas_first}")
print("="*40)

pilihan_kelas=int(input("Kelas yang dipilih (1/2/3) : "))
if pilihan_kelas == 1 :
	harga_tiket=kelas_ekonomi
	jenis_kelas="Ekonomi"
elif pilihan_kelas == 2 :
	harga_tiket=kelas_bisnis
	jenis_kelas="Bisnis"
elif pilihan_kelas == 3 :
	harga_tiket=kelas_first
	jenis_kelas="First"
else:
	print("Pilihan kelas tidak valid")
	
jumlah_tiket=int(input("Jumlah tiket : "))
total_harga=harga_tiket*jumlah_tiket
if jumlah_tiket>3:
	total_harga*=0.8
print("="*70)

#tampilan 4
print("=" * 45)
print(f"| {'STRUK PEMESANAN TIKET PESAWAT':^41} |")
print("=" * 45)
print(f"| {'Nama':<15} : {nama:<23} |")
print(f"| {'Umur':<15} : {umur:<23} |")
print(f"| {'Jenis Kelamin':<15} : {jenis_kelamin:<23} |")
print("-" * 45)
print(f"| {'Kode Maskapai':<15} : {kode_maskapai:<23} |")
print(f"| {'Tujuan':<15} : {tujuan:<23} |")
print(f"| {'Jenis Kelas':<15} : {jenis_kelas:<23} |")
print(f"| {'Jumlah Tiket':<15} : {jumlah_tiket:<23} |")
print(f"| {'Total Harga':<15} : Rp {total_harga:<20} |")
print("="*45)







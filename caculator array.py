def intro():
	print("="*30)
	print("  cacultor array ala Rapli")
	print("="*30)
	print("1. array 1 element")
	print("2. array 2 element")
	print("3. array 3 element")
	print("="*30)
	global ulut
	ulut = int(input("Masukan Angka Yang Ingin di pili\t :"))
	print("="*30)
	prosesif()
def prosesif():
	if ulut == 1:
		array1()
	elif ulut == 2:
		array2()
	elif ulut == 3:
		array3()
		
def array1():
		array1input = int(input("masukan nilai array nya\t :"))
		array1input2 = input("masukan nilai hex contoh 0011 11\t :")
		array1convert = int(array1input2,16)
		print("="*30)
		print("panjang data nilai masukan sesuai angka !")
		print("="*30)
		print("1. char ")
		print("2. int")
		print("3. float")
		print("3. double")
		print("="*30)
		array1input3 = int(input("masukan angka\t :"))
		if array1input3 == 1:
			ucup3 = array1input - 1 
			ucup4 = ucup3 * 1
			ucup1 = ucup4 + array1convert
			ucup2 = hex(ucup1)
			print(ucup2.replace("x","0"))
		elif array1input3 == 2:
			ucup3 = array1input - 1 
			ucup4 = ucup3 * 2
			ucup1 = ucup4 + array1convert
			ucup2 = hex(ucup1)
			print("hasil dari array 1\t :",ucup2.replace("x","0"))
		elif array1input3 == 3:
			ucup3 = array1input - 1 
			ucup4 = ucup3 * 4
			ucup1 = ucup4 + array1convert
			ucup2 = hex(ucup1)
			print("hasil dari array 1\t :",ucup2.replace("x","0"))
		elif array1input3 == 4:
			ucup3 = array1input - 1 
			ucup4 = ucup3 * 8
			ucup1 = ucup4 + array1convert
			ucup2 = hex(ucup1)
			print("hasil dari array 1\t :",ucup2.replace("x","0"))
			
def array2():
		print("="*30)
		print("1. Coloum Major Order / CMO")
		print("2. Baris Major Order / CMO")
		print("="*30)
		
		array2pol = int(input("masukan pilihan\t :"))
		
		if array2pol == 1:
			array2colom()
			
		elif array2pol == 2:
			array2baris()
			
def array2colom():
		j = int(input("Masukan Nilai kolom (j)\t :" ))
		k = int(input("Masukan Nilai Banyak Kolom (k)\t :"))
		i = int(input("Masukan Nilai Baris (i)\t :"))
		hexsadesimal = input("masukan nilai hex contoh 0011 11\t :")
		convert = int(hexsadesimal,16)
		print("="*30)
		print("1. char ")
		print("2. int")
		print("3. float")
		print("4. double")
		print("="*30)
		datanilai = int(input("masukan angka\t :"))
		
		if datanilai == 1:
						hitung1 = j-1
						hitung2 = i-1
						hitung3 = hitung1*k
						hitung4 = hitung2+hitung3
						hitung5 = hitung4*1
						hitung6 = hitung5 + convert
						hitung7 = hex(hitung6)
						print("hasil dari array 2 colom\t :",hitung7.replace("x","0"))
		elif datanilai == 2:
						hitung1 = j-1
						hitung2 = i-1
						hitung3 = hitung1*k
						hitung4 = hitung2+hitung3
						hitung5 = hitung4*2
						hitung6 = hitung5 + convert
						hitung7 = hex(hitung6)
						print("hasil dari array 2 colom\t :",hitung7.replace("x","0"))
		elif datanilai == 3:
						hitung1 = j-1
						hitung2 = i-1
						hitung3 = hitung1*k
						hitung4 = hitung2+hitung3
						hitung5 = hitung4*4
						hitung6 = hitung5 + convert
						hitung7 = hex(hitung6)
						print("hasil dari array 2 colom\t :",hitung7.replace("x","0"))
		elif datanilai == 4:
						hitung1 = j-1
						hitung2 = i-1
						hitung3 = hitung1*k
						hitung4 = hitung2+hitung3
						hitung5 = hitung4*8
						hitung6 = hitung5 + convert
						hitung7 = hex(hitung6)
						print("hasil dari array 2 colom\t :",hitung7.replace("x","0"))
						
def array2baris():
		i = int(input("Masukan Nilai Baris (i)\t :" ))
		n = int(input("Masukan Nilai Banyak Baris (N)\t :"))
		j = int(input("Masukan Nilai Colom (j)\t :"))
		hexsadesimal = input("masukan nilai hex contoh 0011 11\t :")
		convert = int(hexsadesimal,16)
		print("="*30)
		print("1. char ")
		print("2. int")
		print("3. float")
		print("4. double")
		print("="*30)
		datanilai = int(input("masukan angka\t :"))
		
		if datanilai == 1:
						hitung1 = i-1
						hitung2 = j-1
						hitung3 = hitung1*n
						hitung4 = hitung2+hitung3
						hitung5 = hitung4*1
						hitung6 = hitung5 + convert
						hitung7 = hex(hitung6)
						print("hasil dari array 2 Baris\t :",hitung7.replace("x","0"))
		elif datanilai == 2:
						hitung1 = i-1
						hitung2 = j-1
						hitung3 = hitung1*n
						hitung4 = hitung2+hitung3
						hitung5 = hitung4*2
						hitung6 = hitung5 + convert
						hitung7 = hex(hitung6)
						print("hasil dari array 2 Baris\t :",hitung7.replace("x","0"))
		elif datanilai == 3:
						hitung1 = i-1
						hitung2 = j-1
						hitung3 = hitung1*n
						hitung4 = hitung2+hitung3
						hitung5 = hitung4*4
						hitung6 = hitung5 + convert
						hitung7 = hex(hitung6)
						print("hasil dari array 2 Baris\t :",hitung7.replace("x","0"))
		elif datanilai == 4:
						hitung1 = i-1
						hitung2 = j-1
						hitung3 = hitung1*n
						hitung4 = hitung2+hitung3
						hitung5 = hitung4*8
						hitung6 = hitung5 + convert
						hitung7 = hex(hitung6)
						print("hasil dari array 2 Baris\t :",hitung7.replace("x","0"))


def array3():
		m = int(input("Masukan Nilai Pertama (M)\t :" ))
		n = int(input("Masukan Nilai Kedua (N)\t :"))
		p = int(input("Masukan Nilai Ketiga (P)\t :"))
		jumelm2 = int(input("Masukan Nilai Jumlah Elemen2 (Jumelm2)\t :"))
		jumelm3 = int(input("Masukan Nilai Jumlah Elemen3 (Jumelm3)\t :"))
		hexsadesimal = input("masukan nilai hex contoh 0011 11\t :")
		convert = int(hexsadesimal,16)
		print("="*30)
		print("1. char ")
		print("2. int")
		print("3. float")
		print("4. double")
		print("="*30)
		datanilai = int(input("masukan angka\t :"))
		if datanilai == 1:
						hitung = m-1
						hitung1 = jumelm2*jumelm3
						hitung2 = n-1
						hitung3 = p-1
						hitung4 = hitung * hitung1
						hitung5 = hitung2 * jumelm3
						hitung6 = hitung3 + hitung4 +hitung5
						hitung7 = hitung6 * 1
						hitung8 = hitung7 + convert
						hitung9 = hex(hitung8)
						print("hasil dari array 3\t :",hitung9.replace("x","0"))
						
		elif datanilai == 2:
						hitung = m-1
						hitung1 = jumelm2*jumelm3
						hitung2 = n-1
						hitung3 = p-1
						hitung4 = hitung * hitung1
						hitung5 = hitung2 * jumelm3
						hitung6 = hitung3 + hitung4 +hitung5
						hitung7 = hitung6 * 2
						hitung8 = hitung7 + convert
						hitung9 = hex(hitung8)
						print("hasil dari array 3\t :",hitung9.replace("x","0"))
		elif datanilai == 3:
						hitung = m-1
						hitung1 = jumelm2*jumelm3
						hitung2 = n-1
						hitung3 = p-1
						hitung4 = hitung * hitung1
						hitung5 = hitung2 * jumelm3
						hitung6 = hitung3 + hitung4 +hitung5
						hitung7 = hitung6 * 4
						hitung8 = hitung7 + convert
						hitung9 = hex(hitung8)
						print("hasil dari array 3\t :",hitung9.replace("x","0"))
		elif datanilai == 4:
						hitung = m-1
						hitung1 = jumelm2*jumelm3
						hitung2 = n-1
						hitung3 = p-1
						hitung4 = hitung * hitung1
						hitung5 = hitung2 * jumelm3
						hitung6 = hitung3 + hitung4 +hitung5
						hitung7 = hitung6 * 8
						hitung8 = hitung7 + convert
						hitung9 = hex(hitung8)
						print("hasil dari array 3\t :",hitung9.replace("x","0"))
						
						


						
						
						
intro()
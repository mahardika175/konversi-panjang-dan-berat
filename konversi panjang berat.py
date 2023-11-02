def input_satuan():
    print("pilih satuan untuk dikonversi")
    print(" 1. meter")
    print(" 2. gram")
    opsi = int(input("masukkan pilihan : "))
    if opsi == 1 :
        input_meter()
    elif opsi == 2 :
        input_gram()
    else :
        print("mohon hanya pilih 1 atau 2")

def input_meter():
    print("konversi meter")
    print(" 1. meter ke milimeter")
    print(" 2. meter ke centimeter")
    print(" 3. meter ke desimeter")
    print(" 4. meter ke dekameter")
    print(" 5. meter ke hektometer")
    print(" 6. meter ke kilometer")
    print("=" * 25)
    konversi_meter()

def konversi_meter():
    operasi = input("pilih operasi (1/2/3/4/5/6) : ")
    meter = eval(input("masukkan jumlah meter : "))
    print("=" * 25)

    if operasi == "1":
        hasil = meter * 1000
        print(f"hasil konversi dari meter ke milimeter = {hasil:.3f}")
        return hasil

    elif operasi == "2":
        hasil = meter * 100
        print(f"hasil konversi dari meter ke centimeter = = {hasil:.3f}")
        return hasil

    elif operasi == "3":
        hasil = meter * 10
        print(f"hasil konversi dari meter ke desimeter = {hasil:.3f}")
        return hasil

    elif operasi == "4":
        hasil = meter / 10
        print(f"hasil konversi dari meter ke dekameter = {hasil:.3f}")
        return hasil
    
    elif operasi == "5":
        hasil = meter / 100
        print(f"hasil konversi dari meter ke hektometer = {hasil:.3f}")
        return hasil
    
    elif operasi == "6":
        hasil = meter / 1000
        print(f"hasil konversi dari meter ke kilometer = {hasil:.3f}")
        return hasil

    else:
        print("operasi tidak valid")
        return False

def input_gram():
    print("konversi gram")
    print(" 1. gram ke miligram")
    print(" 2. gram ke centigram")
    print(" 3. gram ke desigram")
    print(" 4. gram ke dekagram")
    print(" 5. gram ke hektogram")
    print(" 6. gram ke kilogram")
    print("=" * 25)
    konversi_gram()

def konversi_gram():
    operasi = input("pilih operasi (1/2/3/4/5/6) : ")
    gram = eval(input("masukkan jumlah gram : "))
    print("=" * 25)

    if operasi == "1":
        hasil = gram * 1000
        print(f"hasil konversi dari gram ke miligram = {hasil:.3f}")
        return hasil

    elif operasi == "2":
        hasil = gram * 100
        print(f"hasil konversi dari gram ke centigram = = {hasil:.3f}")
        return hasil

    elif operasi == "3":
        hasil = gram * 10
        print(f"hasil konversi dari gram ke desigram = {hasil:.3f}")
        return hasil

    elif operasi == "4":
        hasil = gram / 10
        print(f"hasil konversi dari gram ke dekagram = {hasil:.3f}")
        return hasil
    
    elif operasi == "5":
        hasil = gram / 100
        print(f"hasil konversi dari gram ke hektogram = {hasil:.3f}")
        return hasil
    
    elif operasi == "6":
        hasil = gram / 1000
        print(f"hasil konversi dari gram ke kilogram = {hasil:.3f}")
        return hasil

    else:
        print("operasi tidak valid")
        return False

input_satuan()
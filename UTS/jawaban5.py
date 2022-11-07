while True:
    nim = int(input(" NIM : "))
    nama = str(input(" Nama : "))
    print (" pilihan menu ")
    print (" 1.Capucino ")
    print (" 2.Teh ")
    print (" 3.Exit ")
    pilihan = int(input(" masukan pilihan "))
    if pilihan == 1:
        print(" memilih capucino ")
        harga = int(input(" masukan harga : "))
        ppn =  harga * 10/100 
        harga_keseluruhan = harga + ppn
        print(" jumlah yang harus dibayarkan : " + str(harga_keseluruhan))
        print("\n")
    elif pilihan == 2:
        print(" memilih teh ")
        harga = int(input(" masukan harga : "))
        ppn = harga * 10/100
        harga_keseluruhan = harga + ppn
        print(" Jumlah yang harus di bayarkan " + str(harga_keseluruhan))
        print("\n")

    else:
        print(" terima kasih sudah mampir ")
        break

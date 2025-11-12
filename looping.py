while True:
    print("=== MENU SEDERHANA ===")
    print("1. Tampilkan 10 bilangan pertama")
    print("2. Tampilkan bilangan genap 1-20")
    print("3. Hitung jumlah 1-100")
    print("4. Keluar")
    
    pilihan = input("Pilih menu: ")
    print("-" * 25)
    
    if pilihan == '1':
        print("10 Bilangan Pertama:")
        for i in range(1, 11):
            print(i, end=" ")
        print("\n")

    elif pilihan == '2':
        print("Bilangan Genap 1-20:")
        for i in range(2, 21, 2):
            print(i, end=" ")
        print("\n")

    elif pilihan == '3':
        print("jumlah 1-100:")
        for i in range(1, 101):
            print(i, end=" ")
        print("\n")
        
    elif pilihan == '4':
        print("Terima kasih, program ditutup.")

    else:
        print("Pilihan tidak valid! Silakan pilih 1-4.\n")
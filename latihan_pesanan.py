import time 



def mengantar_pesanan (pesanan,harga) : 
    
    def start_stopwatch():
        start_time = time.time()
        return start_time

# Fungsi untuk menghentikan stopwatch dan menghitung waktu yang telah berlalu
    def stop_stopwatch(start_time):
        elapsed_time = time.time() - start_time
        return elapsed_time

# Memulai stopwatch
    start_time = start_stopwatch()
    if len(pesanan) < 5 : 

# Contoh penggunaan stopwatch
        time.sleep(5)
    elif len(pesanan) > 5 and len(pesanan) < 15: 
        time.sleep(10) # Menunggu selama 2 detik (Anda bisa mengganti nilainya sesuai kebutuhan)
    else : 
        time.sleep(15)

# Menghentikan stopwatch dan mendapatkan waktu yang telah berlalu
    elapsed_time = stop_stopwatch(start_time)

    for index,makanan in enumerate(pesanan) : 
        if len(pesanan) > 0 : 
            index +=1 
            print(f'pesanan no : {index}')
            print(20*"=")
            print(f'makanan =  {makanan["makanan"]}')
            print(f'harga makanan = {makanan["Harga_makanan"]}\n')
            print(f'Minuman = {makanan["minuman"]}')
            print(f'Minuman = {makanan["Harga_minuman"]}\n')
            
        else  : 
            print("anda tidak punya pesanan")
            exit()
    pesanan.clear()
    print("\n==========TERIMAKASIH SUDAH BERBELANJA==========")
    while True: 
        user_akhir = str(input("apakah anda ingin memesan sesuatu lagi ? (yes/no) = "))
        if user_akhir == "yes" : 
            print('\nOKAY\n')
            main()
        elif user_akhir == "no" :
            exit()
        else : 
            print("jawaban anda tidak valid")
            continue


# Menampilkan waktu yang telah berlalu

def menu (): 
     print("""
           (Makanan)
1. Ikan bakar       6. pizza     
2. Sosis bakar      7. Burger 
3. Ayam Goreng      8. Martabak manis 
4. Bakso Babi       9. Martabak asin 
5. Babi guling      10. Sate lilit   

            (Minuman)
1. air mineral      4. arak bali    
2. Jus anggur       5. wine 
3. Soju             6. Jeruk peras 
   
    """)
def lihat_menu (pesanan,harga): 
    menu()
    while True : 
        user_input = str(input("apakah anda mau memesan sesuatu ? (yes/no = )"))
        user_input.lower()
        if user_input == "yes" : 
            lanjut_pesan(pesanan,harga)
        elif user_input == "no" :
            print("terima kasih sudah berkunjung ke restaurant kami ")
            exit()
        else : 
            print("jawaban anda tidak valid")
            continue



def lanjut_pesan (pesanan,harga) : 
    menu()
    while True : 
    
        plg_makanan  = str(input("Masukan pesananan makanan anda (hanya satu makanan) = "))
        plg_makanan.lower()
        print()
        plg_minuman = str(input("Masukan pesananan minuman anda (hanya satu minuman)  = "))
        plg_minuman.lower()

        hrg_makanan = harga[plg_makanan]
        hrg_minuman = harga[plg_minuman]
        pesanan.append({"makanan":plg_makanan,"Harga_makanan" : hrg_makanan ,"minuman":plg_minuman,"Harga_minuman":hrg_minuman})
        print("\n PESANAN SUDAH DI TAMBAHKAN\n")
        
        user2 = str(input("Apakah ingin memesan lagi (yes/no) = "))
        user2.lower()
        if user2 == "yes": 
            continue
        elif user2 == "no":
            print("Pesanan akan kami buatkan\n cek pesanan anda di opsi(lihat pesanan)\n")            
            break
        else : 
            print("jawaban anda tidak valid, anda akan kembali ke menu utama\n")
            break 
    


    
def tambah_pesanan (pesanan,harga) : 
    if len(pesanan) > 0 : 
        for index,makanan in enumerate(pesanan): 
            index +=1 
            print ("PESANAN ANDA SEBELUM NYA \n")
            print(f'pesanan no : {index}')
            print(10*"=")
            print(f'makanan =  {makanan["makanan"]}')
            print(f'harga makanan = {makanan["Harga_makanan"]}\n')
            print(f'Minuman = {makanan["minuman"]}')
            print(f'Minuman = {makanan["Harga_minuman"]}\n')
            
            
    if len(pesanan)== 0 : 
            print("anda tidak punya pesanan sebelum nya")
    lanjut_pesan(pesanan,harga)
    
def rubah_pesanan (pesanan,harga) : 
    if len(pesanan)== 0 : 
        print("anda tidak punya pesanan, silah pesan di menu utama")
    elif len(pesanan) > 0 : 
        if len(pesanan) == 1 : 
            while True: 
                lihat_pesanan(pesanan)
                print(f'makanan        = {pesanan["makanan"]}')
                print(f'Harga makanan  = {pesanan["Harga_makanan"]}')
                print(f'minuman        = {pesanan["minuman"]}')
                print(f'Harga minuman  = {pesanan["Harga_minuman"]}\n')

                user_rubah = str(input("Opsi apa yang anda akan rubah (makanan/minuman) = "))
                if user_rubah.lower() == "makanan" : 
                    print("""
           (Makanan)
1. Ikan bakar       6. pizza     
2. Sosis bakar      7. Burger 
3. Ayam Goreng      8. Martabak manis 
4. Bakso Babi       9. Martabak asin 
5. Babi guling      10. Sate lilit 

""")
                    print(f'makanan anda sebelum nya adalah {rubah["makanan"]}')
                    user_ganti = str(input("pilih menu makanan,untuk merubah pesanan anda(hanya 1 makanan) = "))
                    rubah["makanan"] = user_ganti
                    rubah["Harga_makanan"] = harga[user_ganti]
                    print("\nPESANAN ANDA SUDAH KAMI RUBAH\n")

                    user_back = str(input(f"apakah ada yang dirubah lagi di pesanan no {user3} (yes/no) = "))
                    if user_back.lower() == "yes" : 
                        continue
                    elif user_back.lower() == "no" : 
                        break
                elif user_rubah.lower() == "minuman" : 
                    print("""
            (Minuman)
1. air mineral      4. arak bali    
2. Jus anggur       5. wine 
3. Soju             6. Jeruk peras 
             
            """)
                    print(f'Minuman anda sebelum nya adalah {rubah["minuman"]}')
                    user_ganti2 = str(input("pilih menu minuman untuk merubah pesanan anda(hanya 1 minuman) = "))
                    rubah["minuman"] = user_ganti2
                    rubah["Harga_minuman"] = harga[user_ganti2]
                    print("\nPESANAN ANDA SUDAH KAMI RUBAH\n")
                    user_back = str(input(f"apakah ada yang dirubah lagi di pesanan no {user3} (yes/no) = "))
                    if user_back.lower() == "yes" : 
                        continue
                    elif user_back.lower() == "no" : 
                        break


        
        while True : 

            lihat_pesanan (pesanan)
            user3 = int(input("Pesanan no berapa yang ada akan rubah ? = "))-1
            rubah = pesanan[user3]
            print(f'makanan        = {rubah["makanan"]}')
            print(f'Harga makanan  = {rubah["Harga_makanan"]}')
            print(f'minuman        = {rubah["minuman"]}')
            print(f'Harga minuman  = {rubah["Harga_minuman"]}\n')

            user_rubah = str(input("Opsi apa yang anda akan rubah (makanan/minuman) = "))
            if user_rubah.lower() == "makanan" : 
                print("""
           (Makanan)
1. Ikan bakar       6. pizza     
2. Sosis bakar      7. Burger 
3. Ayam Goreng      8. Martabak manis 
4. Bakso Babi       9. Martabak asin 
5. Babi guling      10. Sate lilit 

""")
                print(f'makanan anda sebelum nya adalah {rubah["makanan"]}')
                user_ganti = str(input("pilih menu makanan,untuk merubah pesanan anda(hanya 1 makanan) = "))
                rubah["makanan"] = user_ganti
                rubah["Harga_makanan"] = harga[user_ganti]
                print("\nPESANAN ANDA SUDAH KAMI RUBAH\n")

                user_back = str(input(f"apakah ada yang dirubah lagi di pesanan no {user3} (yes/no) = "))
                if user_back.lower() == "yes" : 
                    continue
                elif user_back.lower() == "no" : 
                    break
            elif user_rubah.lower() == "minuman" : 
                print("""
            (Minuman)
1. air mineral      4. arak bali    
2. Jus anggur       5. wine 
3. Soju             6. Jeruk peras 
             
            """)
                print(f'Minuman anda sebelum nya adalah {rubah["minuman"]}')
                user_ganti2 = str(input("pilih menu minuman untuk merubah pesanan anda(hanya 1 minuman) = "))
                rubah["minuman"] = user_ganti2
                rubah["Harga_minuman"] = harga[user_ganti2]
                print("\nPESANAN ANDA SUDAH KAMI RUBAH\n")
                user_back = str(input(f"apakah ada yang dirubah lagi di pesanan no {user3} (yes/no) = "))
                if user_back.lower() == "yes" : 
                    continue
                elif user_back.lower() == "no" : 
                    break


def hapus_pesanan(pesanan): 
    lihat_pesanan(pesanan)
    kesempatan = 0
    if len(pesanan) > 0 : 
        while True : 
            user_hapus = int(input("Pesanan no berapa yang anda akan hapus ? = "))-1
            if user_hapus >= 0 and user_hapus < len(pesanan) : 
                pesanan.pop(user_hapus)
                print("\nPESANAN ANDA SUDAH BERHASIL DI HAPUS")
                user_2 = str(input("Apakah ada pesanan yang anda akan hapus ?(yes/no) = "))
                if user_2.lower() == "yes": 
                    continue
                elif user_2.lower() == "no" : 
                    break

            else : 
                kesempatan +=1
                if kesempatan < 3 : 
                    print("jawaban anda tidak valid\nharap ulang kembali")
                    continue
                elif kesempatan == 3 : 
                    print("jawaban anda tidak valid\nANDA AKAN KEMBALI KE MENU UTAMA")
                    break
            


def lihat_pesanan(pesanan): 
    count = 0 
    for index,makanan in enumerate(pesanan): 
        if len(pesanan) > 0 : 
            index +=1 
            print(f'pesanan no : {index}')
            print(20*"=")
            print(f'makanan =  {makanan["makanan"]}')
            print(f'harga makanan = {makanan["Harga_makanan"]}\n')
            print(f'Minuman = {makanan["minuman"]}')
            print(f'Minuman = {makanan["Harga_minuman"]}\n')
    if len(pesanan) == 0 : 
        while True:
            if len(pesanan) == 0 : 
                user3= str(input("pesanan kamu kosong. apakah kamu mau memesan terlebih dahulu ?(yes/no) = "))
                user3.lower()
                if user3 == "yes": 
                    lanjut_pesan(pesanan)
                elif user3 == "no":
                    break 
            
                else : 
                    count+=1
                    if count == 3 : 
                        print("maaf karna anda sudah menjawab 3 kali secara berulang maka anda di blokir")
                        exit()
                    else : 
                        print("jawaban anda tidak valid harap mengulang\n")
                        continue
            



def main(): 
    pesanan = []
    random = 0 
    harga = {"ikan bakar" : "15.000",
             "sosis bakar":"10.000","ayam goreng":"20.000","bakso babi": "15.00",
             "babi guling" : "25.000", "pizza":"50.000","burger":"18.000","martabak manis":"20.000","martabak asin":"25.000",
             "sate lilit":"30.000","air mineral":"5.000","jus anggur":"20.000","soju":"30.000","arak bali":"35.000","wine":"40.00","jeruk peras": "15.000"}

    while True : 
        print ("Welcome to my restaurant")
        print ("""
1. lihat menu 
2. Pesan makanan/minuman 
3. Tambah pesanan 
4. rubah pesanan 
5. Hapus pesanan 
6. Lihat pesanan saya
7. Saya sudah memesan. dan mau makan
8. Tidak jadi belanja

               
        """)
        pelanggan = str(input("Masukan no opsi yang sesuai dengan keinginan anda = "))
        print()
        if pelanggan == "1" : 
            lihat_menu(pesanan)
        elif pelanggan == "2" : 
            lanjut_pesan (pesanan)
        elif pelanggan == "3" : 
            tambah_pesanan(pesanan)
        elif pelanggan == "4" : 
            rubah_pesanan(pesanan,harga)
        elif pelanggan == "5" : 
            hapus_pesanan(pesanan) 
        elif pelanggan == "6" : 
            lihat_pesanan (pesanan,harga)
        elif pelanggan == "7" : 
            mengantar_pesanan(pesanan,harga)
        elif pelanggan == "8" : 
            print("Terimakasih sudah berkunjung ke restaurant kami ")
            exit()
        else : 
            random+=1
            print('jawaban anda tidak valid')
            if random == 3 : 
                print("maaf anda sudah 3 kali menjawab dengan asal maka anda akan di blokir ")
                exit()
    

if __name__ == "__main__" : 
    main()



























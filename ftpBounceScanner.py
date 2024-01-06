from ftplib import FTP

def ftp_bounce_scan(target_host, bounce_server, bounce_port):
    try:
        # Terhubung ke server FTP
        ftp = FTP()
        ftp.connect(bounce_server, bounce_port)

        # Login dengan kredensial anonim (Anda mungkin perlu menyesuaikannya tergantung pada server)
        ftp.login('anonymous', 'anonymous')

        # Menggunakan PORT atau EPRT untuk membuat koneksi dengan target_host
        ftp.sendcmd(f"PORT {target_host}")

        # Menggunakan perintah LIST dan memeriksa respons
        response = ftp.sendcmd('LIST')

        # Menganalisis respons untuk menentukan apakah port terbuka atau tertutup
        if '150' in response:
            print(f"Port di {target_host} terbuka.")
        elif '425' in response:
            print(f"Port di {target_host} tertutup.")

        # Menutup koneksi FTP
        ftp.quit()

    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def check_ftp_bounce_vulnerability():
    try:
        # Meminta input dari pengguna
        target_host = input("Masukkan alamat IP target (contoh: 172.32.80.80): ")
        bounce_server = input("Masukkan alamat server FTP untuk FTP Bounce: ")
        bounce_port = int(input("Masukkan nomor port server FTP (contoh: 21): "))

        # Membuat koneksi FTP
        ftp = FTP()
        ftp.connect(target_host, bounce_port)

        # Mengirim perintah PORT atau EPRT
        response = ftp.sendcmd(f"PORT {target_host}")

        # Mengecek respon dari server
        if '200' in response:
            print(f"Server pada {target_host} rentan terhadap FTP Bounce.")
            # Memanggil fungsi untuk menjalankan FTP Bounce Scan
            ftp_bounce_scan(target_host, bounce_server, bounce_port)
        else:
            print(f"Server pada {target_host} tidak rentan terhadap FTP Bounce.")

        # Menutup koneksi FTP
        ftp.quit()

    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

# Memanggil fungsi untuk mengecek rentan atau tidak
check_ftp_bounce_vulnerability()

def header():
    """Fungsi untuk menampilkan pesan selamat datang"""
    print("Selamat Datang Di Aplikasi\nPengolahan Data Mahasiswa\n")

def data():
    """Fungsi untuk mengambil data mahasiswa dari pengguna"""
    nama = input("Masukkan nama Anda: ")
    nim = input("Masukkan NIM Anda: ")
    alamat = input("Masukkan alamat Anda: ")
    email = input("Masukkan email Anda: ")

    return nama, nim, alamat, email

def footer():
    """Fungsi untuk menampilkan pesan terima kasih"""
    print("\nTerima Kasih")

# Memanggil fungsi selamat datang
header()

# Memanggil fungsi input_data untuk mengambil data mahasiswa
nama_mahasiswa, nim_mahasiswa, alamat_mahasiswa, email_mahasiswa = data()

# Menampilkan data mahasiswa yang telah diinput
print("\nData Mahasiswa:")
print(f"Nama: {nama_mahasiswa}")
print(f"NIM: {nim_mahasiswa}")
print(f"Alamat: {alamat_mahasiswa}")
print(f"Email: {email_mahasiswa}")

# Memanggil fungsi terima kasih
footer()
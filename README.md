# Pendaftaran Kegiatan Mahasiswa
Aplikasi Pendaftaran Kegiatan Mahasiswa merupakan aplikasi sederhana berbasis Python Tkinter yang digunakan untuk mengisi formulir pendaftaran kegiatan mahasiswa. Aplikasi ini dibuat untuk memenuhi tugas Praktikum Tkinter Sesi 11 tentang Advanced Widgets dan Event Handling.

## 1. Tujuan
Membuat aplikasi GUI menggunakan Python Tkinter dengan menerapkan berbagai widget, pengelolaan event, validasi input, serta penggunaan menu dan dialog.

## 2. Fitur Aplikasi
1. Mengisi nama dan NIM mahasiswa
2. Memilih program studi melalui Combobox
3. Memilih jenis kelamin menggunakan Radiobutton
4. Memilih sistem kuliah, yaitu Reguler, Karyawan, dan Rekognisi Pembelajaran Lampau (RPL)
5. Memilih semester mahasiswa
6. Memilih kegiatan menggunakan Checkbutton
7. Mengisi alasan mengikuti kegiatan
8. Menampilkan hasil pendaftaran
9. Memvalidasi data sebelum disimpan
10. Mencegah pendaftaran menggunakan NIM yang sama
11. Menyimpan data pendaftaran ke file JSON
12. Menghapus formulir dan riwayat pendaftaran menggunakan tombol Reset
13. Mengekspor data pendaftaran
14. Menampilkan notifikasi menggunakan Messagebox
15. Menyediakan menu File dan Bantuan
16. Menampilkan informasi aplikasi melalui halaman About
17. Menggunakan tombol Enter untuk menjalankan Submit

## 3. Teknologi yang Digunakan
| No. | Teknologi | Keterangan |
|---|---|---|
| 1. | Python | Bahasa pemrograman |
| 2. | Tkinter | Membuat tampilan aplikasi |
| 3. | ttk | Menggunakan widget tambahan |
| 4. | JSON | Menyimpan data pendaftaran |

## 4. Struktur Folder
```text
PRAKTIKUM PYTHON TKINTER
│
├── Formulir Kegiatan Mahasiswa.py
├── README.md
├── pendaftaran.json
└── Tampilan Formulir Kegiatan Mahasiswa.png
```

## 5. Cara Menjalankan Aplikasi
1. Pastikan Python sudah terinstal di komputer
2. Buka folder project menggunakan Visual Studio Code
3. Buka terminal pada folder project
4. Jalankan perintah berikut:

```bash
python main.py
```

5. Aplikasi akan terbuka dan siap digunakan

## 6. Menu Aplikasi
| No. | Menu | Fungsi |
|---|---|---|
| 1. | Simpan Data | Menyimpan data pendaftaran |
| 2. | Ekspor Data | Mengekspor data pendaftaran |
| 3. | Reset Data | Menghapus riwayat pendaftaran |
| 4. | Keluar | Menutup aplikasi |
| 5. | About | Menampilkan informasi aplikasi |

## 7. Informasi Praktikum
1. Mata Kuliah: Praktikum Pemrograman Python
2. Materi: Advanced Widgets dan Event Handling
3. Program Studi: Teknik Informatika
4. Fakultas: Teknologi Informasi
5. Universitas: Hasyim Asy'ari
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Formulir Identitas Mahasiswa")
root.geometry("900x650")
root.resizable(False, False)

# Warna aplikasi
warna_bg = "#EAF2F8"
warna_putih = "#FFFFFF"
warna_biru = "#2874A6"
warna_biru_tua = "#1F4E79"
warna_teks = "#243746"
warna_abu = "#7F8C8D"
warna_merah = "#C0392B"

root.configure(bg=warna_bg)

# Frame utama
frame_utama = tk.Frame(root, bg=warna_bg)
frame_utama.pack(fill="both", expand=True, padx=25, pady=10)

# Judul
judul = tk.Label(
    frame_utama,
    text="FORMULIR IDENTITAS MAHASISWA",
    font=("Arial", 15, "bold"),
    bg=warna_bg,
    fg=warna_biru_tua
)
judul.pack(pady=(5, 2))

subjudul = tk.Label(
    frame_utama,
    text="FAKULTAS TEKNOLOGI INFORMASI\nUNIVERSITAS HASYIM ASY'ARI",
    font=("Arial", 11, "bold"),
    bg=warna_bg,
    fg=warna_biru_tua
)
subjudul.pack(pady=(0, 10))

# Formulir identitas
frame_form = tk.Frame(
    frame_utama,
    bg=warna_putih,
    padx=15,
    pady=8
)
frame_form.pack(fill="x", padx=30)

frame_form.grid_columnconfigure(0, minsize=130)
frame_form.grid_columnconfigure(1, minsize=15)
frame_form.grid_columnconfigure(2, weight=1)

def buat_label(teks, baris):
    tk.Label(
        frame_form,
        text=teks,
        font=("Arial", 10, "bold"),
        bg=warna_putih,
        fg=warna_teks
    ).grid(row=baris, column=0, sticky="w", padx=5, pady=5)

    tk.Label(
        frame_form,
        text=":",
        font=("Arial", 10),
        bg=warna_putih,
        fg=warna_teks
    ).grid(row=baris, column=1, pady=5)

# Nama
buat_label("Nama", 0)

entry_nama = tk.Entry(
    frame_form,
    font=("Arial", 10),
    relief="solid",
    bd=1
)
entry_nama.grid(row=0, column=2, sticky="ew", padx=8, pady=5, ipady=3)

# NIM
buat_label("NIM", 1)

entry_nim = tk.Entry(
    frame_form,
    font=("Arial", 10),
    relief="solid",
    bd=1
)
entry_nim.grid(row=1, column=2, sticky="ew", padx=8, pady=5, ipady=3)

# Jenis kelamin
buat_label("Jenis Kelamin", 2)

frame_gender = tk.Frame(frame_form, bg=warna_putih)
frame_gender.grid(row=2, column=2, sticky="w", padx=8, pady=5)

laki_var = tk.BooleanVar()
perempuan_var = tk.BooleanVar()

def pilih_laki():
    if laki_var.get():
        perempuan_var.set(False)

def pilih_perempuan():
    if perempuan_var.get():
        laki_var.set(False)

tk.Checkbutton(
    frame_gender,
    text="Laki-laki",
    variable=laki_var,
    command=pilih_laki,
    font=("Arial", 9),
    bg=warna_putih,
    activebackground=warna_putih
).pack(side="left", padx=(0, 15))

tk.Checkbutton(
    frame_gender,
    text="Perempuan",
    variable=perempuan_var,
    command=pilih_perempuan,
    font=("Arial", 9),
    bg=warna_putih,
    activebackground=warna_putih
).pack(side="left")

# Program studi
buat_label("Program Studi", 3)

combo_prodi = ttk.Combobox(
    frame_form,
    font=("Arial", 9),
    state="readonly",
    values=[
        "Teknik Informatika",
        "Sistem Informasi",
        "Teknologi Informasi"
    ]
)
combo_prodi.grid(row=3, column=2, sticky="ew", padx=8, pady=5)

# Sistem kuliah
buat_label("Sistem Kuliah", 4)

combo_sistem = ttk.Combobox(
    frame_form,
    font=("Arial", 9),
    state="readonly",
    values=[
        "Reguler",
        "Karyawan",
        "Rekognisi Pembelajaran Lampau"
    ]
)
combo_sistem.grid(row=4, column=2, sticky="ew", padx=8, pady=5)

# Semester
buat_label("Semester", 5)

combo_semester = ttk.Combobox(
    frame_form,
    font=("Arial", 9),
    state="readonly",
    values=[
        "Semester 1",
        "Semester 2",
        "Semester 3",
        "Semester 4",
        "Semester 5",
        "Semester 6",
        "Semester 7",
        "Semester 8"
    ]
)
combo_semester.grid(row=5, column=2, sticky="ew", padx=8, pady=5)

# Tombol
frame_tombol = tk.Frame(frame_utama, bg=warna_bg)
frame_tombol.pack(pady=12)

# Hasil identitas
judul_hasil = tk.Label(
    frame_utama,
    text="HASIL IDENTITAS MAHASISWA",
    font=("Arial", 12, "bold"),
    bg=warna_bg,
    fg=warna_biru_tua
)
judul_hasil.pack(pady=(3, 7))

frame_hasil = tk.Frame(
    frame_utama,
    bg=warna_putih,
    padx=10,
    pady=7
)
frame_hasil.pack(fill="x", padx=30)

frame_hasil.grid_columnconfigure(0, minsize=130)
frame_hasil.grid_columnconfigure(1, minsize=15)
frame_hasil.grid_columnconfigure(2, weight=1)

def tampilkan_placeholder():
    for widget in frame_hasil.winfo_children():
        widget.destroy()

    tk.Label(
        frame_hasil,
        text="Hasil input akan ditampilkan di sini.",
        font=("Arial", 9),
        bg=warna_putih,
        fg=warna_abu
    ).grid(row=0, column=0, columnspan=3, sticky="w", padx=5, pady=3)

tampilkan_placeholder()

# Fungsi simpan
def simpan():
    nama = entry_nama.get().strip()
    nim = entry_nim.get().strip()
    prodi = combo_prodi.get()
    sistem = combo_sistem.get()
    semester = combo_semester.get()

    if laki_var.get():
        gender = "Laki-laki"
    elif perempuan_var.get():
        gender = "Perempuan"
    else:
        gender = ""

    if not nama or not nim or not gender or not prodi or not sistem or not semester:
        messagebox.showwarning(
            "Peringatan",
            "Semua data harus diisi terlebih dahulu!"
        )
        return

    for widget in frame_hasil.winfo_children():
        widget.destroy()

    data = [
        ("Nama", nama),
        ("NIM", nim),
        ("Jenis Kelamin", gender),
        ("Program Studi", prodi),
        ("Sistem Kuliah", sistem),
        ("Semester", semester)
    ]

    for i, (label, nilai) in enumerate(data):
        tk.Label(
            frame_hasil,
            text=label,
            font=("Arial", 9, "bold"),
            bg=warna_putih,
            fg=warna_teks,
            anchor="w"
        ).grid(row=i, column=0, sticky="nw", padx=5, pady=4)

        tk.Label(
            frame_hasil,
            text=":",
            font=("Arial", 9),
            bg=warna_putih,
            fg=warna_teks
        ).grid(row=i, column=1, sticky="nw", padx=5, pady=4)

        tk.Label(
            frame_hasil,
            text=nilai,
            font=("Arial", 9),
            bg=warna_putih,
            fg=warna_teks,
            anchor="w",
            justify="left",
            wraplength=550
        ).grid(row=i, column=2, sticky="w", padx=5, pady=4)

    messagebox.showinfo(
        "Berhasil",
        "Data identitas mahasiswa berhasil disimpan!"
    )

# Fungsi reset
def reset():
    entry_nama.delete(0, tk.END)
    entry_nim.delete(0, tk.END)

    laki_var.set(False)
    perempuan_var.set(False)

    combo_prodi.set("")
    combo_sistem.set("")
    combo_semester.set("")

    tampilkan_placeholder()

# Fungsi keluar
def keluar():
    konfirmasi = messagebox.askyesno(
        "Keluar",
        "Apakah Anda yakin ingin keluar?"
    )

    if konfirmasi:
        root.destroy()

# Tombol simpan
tk.Button(
    frame_tombol,
    text="Simpan",
    font=("Arial", 9, "bold"),
    bg=warna_biru,
    fg=warna_putih,
    width=12,
    relief="flat",
    cursor="hand2",
    command=simpan
).pack(side="left", padx=7, ipady=5)

# Tombol reset
tk.Button(
    frame_tombol,
    text="Reset",
    font=("Arial", 9, "bold"),
    bg=warna_abu,
    fg=warna_putih,
    width=12,
    relief="flat",
    cursor="hand2",
    command=reset
).pack(side="left", padx=7, ipady=5)

# Tombol keluar
tk.Button(
    frame_tombol,
    text="Keluar",
    font=("Arial", 9, "bold"),
    bg=warna_merah,
    fg=warna_putih,
    width=12,
    relief="flat",
    cursor="hand2",
    command=keluar
).pack(side="left", padx=7, ipady=5)

root.mainloop()
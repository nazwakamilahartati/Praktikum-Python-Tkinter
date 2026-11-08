
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os

# Jendela utama
root = tk.Tk()
root.title("Formulir Pendaftaran Kegiatan Mahasiswa")
root.geometry("850x650")
root.resizable(False, False)

# Warna aplikasi
warna_bg = "#EAF2F8"
warna_putih = "#FFFFFF"
warna_biru = "#2874A6"
warna_biru_tua = "#1F4E79"
warna_teks = "#243746"
warna_abu = "#7F8C8D"

root.configure(bg=warna_bg)

# File penyimpanan
file_data = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "pendaftaran.json"
)

riwayat = []

# Variabel formulir
nama = tk.StringVar()
nim = tk.StringVar()
gender = tk.StringVar()
prodi = tk.StringVar()
sistem = tk.StringVar()
semester = tk.StringVar()

kegiatan = {
    "Seminar Teknologi": tk.BooleanVar(),
    "Workshop Python": tk.BooleanVar(),
    "Pelatihan Desain": tk.BooleanVar(),
    "Bakti Sosial": tk.BooleanVar()
}

# Membaca data JSON
def muat_data():
    global riwayat

    if os.path.exists(file_data):
        try:
            with open(file_data, "r", encoding="utf-8") as file:
                data = json.load(file)

                if isinstance(data, list):
                    riwayat = data

        except (json.JSONDecodeError, OSError):
            riwayat = []

# Menyimpan data JSON
def simpan_data():
    with open(file_data, "w", encoding="utf-8") as file:
        json.dump(
            riwayat,
            file,
            indent=4,
            ensure_ascii=False
        )

# Simpan melalui menu File
def simpan_manual():
    try:
        simpan_data()
        messagebox.showinfo(
            "Berhasil",
            "Data pendaftaran berhasil disimpan."
        )

    except OSError:
        messagebox.showerror(
            "Gagal",
            "Data tidak dapat disimpan."
        )

# Ekspor data
def ekspor_data():
    if not riwayat:
        messagebox.showwarning(
            "Peringatan",
            "Belum ada data yang dapat diekspor."
        )
        return

    lokasi = filedialog.asksaveasfilename(
        title="Ekspor Data Pendaftaran",
        defaultextension=".json",
        filetypes=[("File JSON", "*.json")],
        initialfile="data_pendaftaran.json"
    )

    if lokasi:
        try:
            with open(lokasi, "w", encoding="utf-8") as file:
                json.dump(
                    riwayat,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            messagebox.showinfo(
                "Berhasil",
                "Data berhasil diekspor."
            )

        except OSError:
            messagebox.showerror(
                "Gagal",
                "Data tidak dapat diekspor."
            )

# Menampilkan kegiatan yang dipilih
def tampilkan_kegiatan():
    list_kegiatan.delete(0, tk.END)

    for item, nilai in kegiatan.items():
        if nilai.get():
            list_kegiatan.insert(tk.END, item)

# Menampilkan hasil pendaftaran
def tampilkan_riwayat():
    output.config(state="normal")
    output.delete("1.0", tk.END)

    if not riwayat:
        output.insert(
            tk.END,
            "Belum ada data pendaftaran."
        )

    else:
        for nomor, data in enumerate(riwayat, start=1):

            output.insert(
                tk.END,
                f"DATA PENDAFTAR {nomor}\n",
                "subjudul"
            )

            daftar_data = [
                ("Nama", data.get("nama", "-")),
                ("NIM", data.get("nim", "-")),
                ("Jenis Kelamin", data.get("gender", "-")),
                ("Program Studi", data.get("prodi", "-")),
                ("Sistem Kuliah", data.get("sistem", "-")),
                ("Semester", data.get("semester", "-")),
                (
                    "Kegiatan",
                    ", ".join(data.get("kegiatan", []))
                ),
                ("Alasan Mengikuti", data.get("alasan", "-"))
            ]

            for label, nilai in daftar_data:
                output.insert(
                    tk.END,
                    f"{label:<20} : {nilai}\n"
                )

            output.insert(tk.END, "\n")

    # Tampilkan hasil dari bagian awal
    output.config(state="disabled")
    output.yview_moveto(0)

# Mengosongkan formulir
def kosongkan_form():
    nama.set("")
    nim.set("")
    gender.set("")
    prodi.set("")
    sistem.set("")
    semester.set("")

    for nilai in kegiatan.values():
        nilai.set(False)

    text_alasan.delete("1.0", tk.END)
    list_kegiatan.delete(0, tk.END)

    entry_nama.focus()

# Fungsi Submit
def submit():
    nama_mahasiswa = nama.get().strip()
    nomor_induk = nim.get().strip()

    if not nama_mahasiswa:
        messagebox.showwarning(
            "Peringatan",
            "Nama mahasiswa tidak boleh kosong."
        )
        entry_nama.focus()
        return

    if not nomor_induk:
        messagebox.showwarning(
            "Peringatan",
            "NIM tidak boleh kosong."
        )
        entry_nim.focus()
        return

    # Memeriksa NIM yang sudah terdaftar
    for data in riwayat:
        if data.get("nim") == nomor_induk:
            messagebox.showwarning(
                "Peringatan",
                "NIM tersebut sudah terdaftar."
            )
            entry_nim.focus()
            return

    if not gender.get():
        messagebox.showwarning(
            "Peringatan",
            "Silakan pilih jenis kelamin."
        )
        return

    if not prodi.get():
        messagebox.showwarning(
            "Peringatan",
            "Silakan pilih program studi."
        )
        return

    if not sistem.get():
        messagebox.showwarning(
            "Peringatan",
            "Silakan pilih sistem kuliah."
        )
        return

    if not semester.get():
        messagebox.showwarning(
            "Peringatan",
            "Silakan pilih semester."
        )
        return

    pilihan = [
        item for item, nilai in kegiatan.items()
        if nilai.get()
    ]

    if not pilihan:
        messagebox.showwarning(
            "Peringatan",
            "Silakan pilih minimal satu kegiatan."
        )
        return

    alasan = text_alasan.get("1.0", tk.END).strip()

    data_baru = {
        "nama": nama_mahasiswa,
        "nim": nomor_induk,
        "gender": gender.get(),
        "prodi": prodi.get(),
        "sistem": sistem.get(),
        "semester": semester.get(),
        "kegiatan": pilihan,
        "alasan": alasan if alasan else "-"
    }

    riwayat.append(data_baru)

    try:
        simpan_data()

    except OSError:
        riwayat.pop()

        messagebox.showerror(
            "Gagal",
            "Data pendaftaran tidak dapat disimpan."
        )
        return

    tampilkan_riwayat()

    messagebox.showinfo(
        "Berhasil",
        "Data pendaftaran mahasiswa berhasil disimpan."
    )

    kosongkan_form()

# Reset formulir dan seluruh riwayat
def reset_form():
    global riwayat

    konfirmasi = messagebox.askyesno(
        "Konfirmasi Reset",
        "Apakah Anda yakin ingin menghapus seluruh "
        "isian formulir dan riwayat pendaftaran?"
    )

    if konfirmasi:
        data_lama = riwayat.copy()
        riwayat = []

        try:
            simpan_data()

        except OSError:
            riwayat = data_lama

            messagebox.showerror(
                "Gagal",
                "Data tidak dapat dihapus."
            )
            return

        kosongkan_form()
        tampilkan_riwayat()

        messagebox.showinfo(
            "Berhasil",
            "Seluruh formulir dan riwayat berhasil di-reset."
        )

# Menghapus riwayat melalui menu File
def reset_data():
    global riwayat

    if not riwayat:
        messagebox.showinfo(
            "Informasi",
            "Belum ada data pendaftaran yang tersimpan."
        )
        return

    konfirmasi = messagebox.askyesno(
        "Konfirmasi Hapus Data",
        "Apakah Anda yakin ingin menghapus seluruh "
        "riwayat pendaftaran?"
    )

    if konfirmasi:
        data_lama = riwayat.copy()
        riwayat = []

        try:
            simpan_data()

        except OSError:
            riwayat = data_lama

            messagebox.showerror(
                "Gagal",
                "Data tidak dapat dihapus."
            )
            return

        tampilkan_riwayat()

        messagebox.showinfo(
            "Berhasil",
            "Seluruh riwayat pendaftaran berhasil dihapus."
        )

# Keluar aplikasi
def keluar():
    konfirmasi = messagebox.askyesno(
        "Keluar",
        "Apakah Anda yakin ingin keluar dari aplikasi?"
    )

    if konfirmasi:
        root.destroy()

# Jendela About
def about():
    jendela = tk.Toplevel(root)
    jendela.title("Tentang Aplikasi")
    jendela.geometry("500x560")
    jendela.resizable(False, False)
    jendela.configure(bg=warna_bg)

    tk.Label(
        jendela,
        text="TENTANG APLIKASI",
        font=("Arial", 16, "bold"),
        bg=warna_bg,
        fg=warna_biru_tua
    ).pack(pady=(15, 10))

    frame_about = tk.Frame(
        jendela,
        bg=warna_putih,
        padx=20,
        pady=10
    )

    frame_about.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=(0, 10)
    )

    tk.Label(
        frame_about,
        text="Pendaftaran Kegiatan Mahasiswa",
        font=("Arial", 13, "bold"),
        bg=warna_putih,
        fg=warna_biru_tua
    ).pack(pady=(5, 8))

    tk.Label(
        frame_about,
        text="Aplikasi ini dibuat untuk membantu mahasiswa "
             "melakukan pendaftaran kegiatan melalui formulir "
             "berbasis GUI menggunakan Python Tkinter.",
        font=("Arial", 9),
        bg=warna_putih,
        fg=warna_teks,
        wraplength=400,
        justify="center"
    ).pack(pady=(0, 10))

    tk.Label(
        frame_about,
        text="FITUR APLIKASI",
        font=("Arial", 10, "bold"),
        bg=warna_putih,
        fg=warna_biru_tua
    ).pack(pady=(3, 5))

    daftar_fitur = [
        "1. Input identitas mahasiswa dan NIM",
        "2. Pilihan program studi dan sistem kuliah",
        "3. Pemilihan semester dan jenis kelamin",
        "4. Pilihan kegiatan dan alasan mengikuti",
        "5. Penyimpanan dan tampilan hasil pendaftaran",
        "6. Validasi, Messagebox, dan event keyboard"
    ]

    for fitur in daftar_fitur:
        tk.Label(
            frame_about,
            text=fitur,
            font=("Arial", 9),
            bg=warna_putih,
            fg=warna_teks
        ).pack(pady=1)

    tk.Label(
        frame_about,
        text="TEKNOLOGI YANG DIGUNAKAN",
        font=("Arial", 10, "bold"),
        bg=warna_putih,
        fg=warna_biru_tua
    ).pack(pady=(10, 5))

    tk.Label(
        frame_about,
        text="Python  |  Tkinter  |  ttk  |  JSON",
        font=("Arial", 9),
        bg=warna_putih,
        fg=warna_teks
    ).pack(pady=2)

    tk.Label(
        frame_about,
        text="Praktikum Tkinter Sesi 11\n"
             "Advanced Widgets dan Event Handling",
        font=("Arial", 9),
        bg=warna_putih,
        fg=warna_abu,
        justify="center"
    ).pack(pady=(2, 8))

    tk.Label(
        frame_about,
        text="Program Studi Teknik Informatika\n"
             "Fakultas Teknologi Informasi\n"
             "Universitas Hasyim Asy'ari",
        font=("Arial", 9, "bold"),
        bg=warna_putih,
        fg=warna_biru_tua,
        justify="center"
    ).pack(pady=(5, 3))

    tk.Button(
        jendela,
        text="Tutup",
        command=jendela.destroy,
        bg=warna_biru,
        fg=warna_putih,
        font=("Arial", 9, "bold"),
        width=15,
        relief="flat",
        cursor="hand2"
    ).pack(pady=(0, 10))

# Menu aplikasi
menu_bar = tk.Menu(root)

menu_file = tk.Menu(menu_bar, tearoff=0)

menu_file.add_command(
    label="Simpan Data",
    command=simpan_manual
)

menu_file.add_command(
    label="Ekspor Data",
    command=ekspor_data
)

menu_file.add_command(
    label="Reset Data",
    command=reset_data
)

menu_file.add_separator()

menu_file.add_command(
    label="Keluar",
    command=keluar
)

menu_bar.add_cascade(
    label="File",
    menu=menu_file
)

menu_bantuan = tk.Menu(menu_bar, tearoff=0)

menu_bantuan.add_command(
    label="About",
    command=about
)

menu_bar.add_cascade(
    label="Bantuan",
    menu=menu_bantuan
)

root.config(menu=menu_bar)

# Area utama dengan scroll
frame_utama = tk.Frame(root, bg=warna_bg)
frame_utama.pack(fill="both", expand=True)

canvas = tk.Canvas(
    frame_utama,
    bg=warna_bg,
    highlightthickness=0
)

scrollbar = ttk.Scrollbar(
    frame_utama,
    orient="vertical",
    command=canvas.yview
)

canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

frame_isi = tk.Frame(canvas, bg=warna_bg)

window_id = canvas.create_window(
    (0, 0),
    window=frame_isi,
    anchor="nw"
)

def update_scroll(event):
    canvas.configure(
        scrollregion=canvas.bbox("all")
    )

def atur_lebar(event):
    canvas.itemconfig(
        window_id,
        width=event.width
    )

frame_isi.bind("<Configure>", update_scroll)
canvas.bind("<Configure>", atur_lebar)

# Scroll mouse
def scroll_mouse(event):
    widget = root.winfo_containing(
        event.x_root,
        event.y_root
    )

    if widget is None:
        return

    nama_widget = str(widget)

    if nama_widget.startswith(str(output)):
        output.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )
    else:
        canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )

root.bind_all("<MouseWheel>", scroll_mouse)

# Judul aplikasi
tk.Label(
    frame_isi,
    text="FORMULIR PENDAFTARAN KEGIATAN MAHASISWA",
    font=("Arial", 12, "bold"),
    bg=warna_bg,
    fg=warna_biru_tua
).pack(pady=(5, 1))

tk.Label(
    frame_isi,
    text="FAKULTAS TEKNOLOGI INFORMASI\n"
         "UNIVERSITAS HASYIM ASY'ARI",
    font=("Arial", 9, "bold"),
    bg=warna_bg,
    fg=warna_biru_tua
).pack(pady=(0, 4))

# Formulir identitas
frame_form = tk.Frame(
    frame_isi,
    bg=warna_putih,
    padx=8,
    pady=2
)

frame_form.pack(
    fill="x",
    padx=30
)

frame_form.grid_columnconfigure(0, minsize=130)
frame_form.grid_columnconfigure(1, minsize=15)
frame_form.grid_columnconfigure(2, weight=1)

def buat_label(teks, baris):
    tk.Label(
        frame_form,
        text=teks,
        font=("Arial", 9, "bold"),
        bg=warna_putih,
        fg=warna_teks
    ).grid(
        row=baris,
        column=0,
        sticky="w",
        padx=5,
        pady=1
    )

    tk.Label(
        frame_form,
        text=":",
        font=("Arial", 9),
        bg=warna_putih,
        fg=warna_teks
    ).grid(
        row=baris,
        column=1,
        pady=1
    )

# Nama
buat_label("Nama", 0)

entry_nama = tk.Entry(
    frame_form,
    font=("Arial", 9),
    relief="solid",
    bd=1,
    textvariable=nama
)

entry_nama.grid(
    row=0,
    column=2,
    sticky="ew",
    padx=8,
    pady=1,
    ipady=1
)

# NIM
buat_label("NIM", 1)

entry_nim = tk.Entry(
    frame_form,
    font=("Arial", 9),
    relief="solid",
    bd=1,
    textvariable=nim
)

entry_nim.grid(
    row=1,
    column=2,
    sticky="ew",
    padx=8,
    pady=1,
    ipady=1
)

# Jenis kelamin
buat_label("Jenis Kelamin", 2)

frame_gender = tk.Frame(
    frame_form,
    bg=warna_putih
)

frame_gender.grid(
    row=2,
    column=2,
    sticky="w",
    padx=8,
    pady=1
)

tk.Radiobutton(
    frame_gender,
    text="Laki-laki",
    variable=gender,
    value="Laki-laki",
    font=("Arial", 9),
    bg=warna_putih,
    activebackground=warna_putih
).pack(side="left", padx=(0, 15))

tk.Radiobutton(
    frame_gender,
    text="Perempuan",
    variable=gender,
    value="Perempuan",
    font=("Arial", 9),
    bg=warna_putih,
    activebackground=warna_putih
).pack(side="left")

# Program studi
buat_label("Program Studi", 3)

combo_prodi = ttk.Combobox(
    frame_form,
    font=("Arial", 9),
    textvariable=prodi,
    state="readonly",
    values=[
        "Teknik Informatika",
        "Sistem Informasi",
        "Teknologi Informasi"
    ]
)

combo_prodi.grid(
    row=3,
    column=2,
    sticky="ew",
    padx=8,
    pady=1
)

# Sistem kuliah
buat_label("Sistem Kuliah", 4)

combo_sistem = ttk.Combobox(
    frame_form,
    font=("Arial", 9),
    textvariable=sistem,
    state="readonly",
    values=[
        "Reguler",
        "Karyawan",
        "Rekognisi Pembelajaran Lampau"
    ]
)

combo_sistem.grid(
    row=4,
    column=2,
    sticky="ew",
    padx=8,
    pady=1
)

# Semester
buat_label("Semester", 5)

combo_semester = ttk.Combobox(
    frame_form,
    font=("Arial", 9),
    textvariable=semester,
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

combo_semester.grid(
    row=5,
    column=2,
    sticky="ew",
    padx=8,
    pady=1
)

# Pilihan kegiatan
buat_label("Pilih Kegiatan", 6)

frame_kegiatan = tk.Frame(
    frame_form,
    bg=warna_putih
)

frame_kegiatan.grid(
    row=6,
    column=2,
    sticky="w",
    padx=8,
    pady=1
)

for item, nilai in kegiatan.items():
    tk.Checkbutton(
        frame_kegiatan,
        text=item,
        variable=nilai,
        command=tampilkan_kegiatan,
        font=("Arial", 9),
        bg=warna_putih,
        activebackground=warna_putih
    ).pack(anchor="w")

# Listbox kegiatan
buat_label("Kegiatan Dipilih", 7)

list_kegiatan = tk.Listbox(
    frame_form,
    height=2,
    font=("Arial", 9),
    relief="solid",
    bd=1,
    bg="#F4F8FC"
)

list_kegiatan.grid(
    row=7,
    column=2,
    sticky="ew",
    padx=8,
    pady=1
)

# Alasan mengikuti
buat_label("Alasan Mengikuti", 8)

text_alasan = tk.Text(
    frame_form,
    height=2,
    font=("Arial", 9),
    relief="solid",
    bd=1,
    bg="#F4F8FC",
    wrap="word"
)

text_alasan.grid(
    row=8,
    column=2,
    sticky="ew",
    padx=8,
    pady=1
)

# Tombol Submit dan Reset
frame_tombol = tk.Frame(
    frame_isi,
    bg=warna_bg
)

frame_tombol.pack(pady=3)

tk.Button(
    frame_tombol,
    text="Submit",
    font=("Arial", 9, "bold"),
    bg=warna_biru,
    fg=warna_putih,
    width=12,
    relief="flat",
    cursor="hand2",
    command=submit
).pack(side="left", padx=7, ipady=3)

tk.Button(
    frame_tombol,
    text="Reset",
    font=("Arial", 9, "bold"),
    bg=warna_abu,
    fg=warna_putih,
    width=12,
    relief="flat",
    cursor="hand2",
    command=reset_form
).pack(side="left", padx=7, ipady=3)

# Judul hasil
tk.Label(
    frame_isi,
    text="HASIL PENDAFTARAN MAHASISWA",
    font=("Arial", 11, "bold"),
    bg=warna_bg,
    fg=warna_biru_tua
).pack(pady=(2, 3))

# Frame hasil
frame_hasil = tk.Frame(
    frame_isi,
    bg=warna_putih,
    padx=8,
    pady=3
)

frame_hasil.pack(
    fill="x",
    padx=30,
    pady=(0, 5)
)

# Scrollbar hasil
frame_output = tk.Frame(
    frame_hasil,
    bg=warna_putih
)

frame_output.pack(
    fill="both",
    expand=True
)

scroll_hasil = ttk.Scrollbar(
    frame_output,
    orient="vertical"
)

scroll_hasil.pack(
    side="right",
    fill="y"
)

# Area hasil pendaftaran
output = tk.Text(
    frame_output,
    height=13,
    font=("Consolas", 9),
    bg=warna_putih,
    fg=warna_teks,
    relief="flat",
    padx=5,
    pady=3,
    wrap="word",
    state="disabled",
    yscrollcommand=scroll_hasil.set
)

output.pack(
    side="left",
    fill="both",
    expand=True
)

scroll_hasil.config(command=output.yview)

output.tag_config(
    "subjudul",
    font=("Arial", 10, "bold"),
    foreground=warna_biru_tua
)

# Enter untuk Submit
entry_nama.bind(
    "<Return>",
    lambda event: submit()
)

entry_nim.bind(
    "<Return>",
    lambda event: submit()
)

# Memuat data saat aplikasi dibuka
muat_data()
tampilkan_riwayat()

root.mainloop()
# Modul 8 GUI Programming
# tkinter, tkcalendar
import datetime  # menangani tanggal dan waktu
from tkinter import *  # GUI
import tkinter.messagebox as mb  # kotak pesan
from tkinter import ttk  # widget tambahan
from tkcalendar import DateEntry  # widget kalender
import sqlite3  # menangani database SQLite

# Konfigurasi font
headlabelfont = ("Montserrat", 16, 'bold')
labelfont = ('Arial', 14)
entryfont = ('Arial', 12)

# Membuat koneksi ke database SQLite
connector = sqlite3.connect('SchoolManagement.db')
# Membuat cursor untuk eksekusi query
cursor = connector.cursor()
# Membuat tabel MANAJEMEN_MAHASISWA jika belum ada
connector.execute(
    "CREATE TABLE IF NOT EXISTS MANAJEMEN_MAHASISWA (NAMA TEXT, EMAIL TEXT, NO_TELEPON TEXT, JENIS_KELAMIN TEXT, TGL_LAHIR TEXT, JURUSAN TEXT)"
)
# Modul 5 Class dan Constructor (Object Oriented Programming 1)
# Class: SchoolManagementSystem
# Constructor: __init__
# Class ini digunakan untuk mengorganisir seluruh sistem manajemen dalam sebuah objek, dan constructor digunakan untuk inisialisasi UI dan variabel.
# Kelas utama untuk Sistem Manajemen Sekolah
class SchoolManagementSystem:
    # Konstruktor dengan parameter master yang merupakan root window
    def __init__(self, master):
        self.master = master
        self.master.title('Sistem Manajemen Mahasiswa')  # Judul window
        self.master.geometry('1300x600')  # Ukuran window
        self.master.resizable(0, 0)  # Window tidak bisa di-resize

        self.lf_bg = '#e6e6fa'  # Lavender
        self.cf_bg = '#f0e6fa'  # Lavender Blush
        self.rf_bg = '#ffe4e1'  # Misty Rose

# Modul 1 Variabel, Tipe Data, dan Array
# Variabel: name_strvar, email_strvar, contact_strvar, gender_strvar, stream_strvar, dob
# Tipe Data: StringVar, DateEntry, String, Date
        # Inisialisasi variabel yang digunakan dalam UI
        self.name_strvar = StringVar()
        self.email_strvar = StringVar()
        self.contact_strvar = StringVar()
        self.gender_strvar = StringVar()
        self.stream_strvar = StringVar()

        self.setup_ui()  # Memanggil fungsi setup_ui untuk setup tampilan

# Modul 4 Function dan Method
# Function/Method: setup_ui, reset_fields, display_records, add_record, remove_record, view_record
    # Fungsi untuk mengatur tampilan antarmuka pengguna
    def setup_ui(self):
        # Membuat frame dan widget untuk tampilan
        Label(self.master, text="SISTEM MANAJEMEN MAHASISWA", font=headlabelfont, bg='navy', fg='white').pack(side=TOP, fill=X)
        left_frame = Frame(self.master, bg=self.lf_bg)
        left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)
        center_frame = Frame(self.master, bg=self.cf_bg)
        center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
        right_frame = Frame(self.master, bg=self.rf_bg)
        right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)

        # Membuat label dan entry fields untuk data mahasiswa
        Label(left_frame, text="Nama", font=labelfont, bg=self.lf_bg, anchor='w').place(relx=0.05, rely=0.05, relwidth=0.9)
        Label(left_frame, text="Nomor Kontak", font=labelfont, bg=self.lf_bg, anchor='w').place(relx=0.05, rely=0.18, relwidth=0.9)
        Label(left_frame, text="Email", font=labelfont, bg=self.lf_bg, anchor='w').place(relx=0.05, rely=0.31, relwidth=0.9)
        Label(left_frame, text="Jenis Kelamin", font=labelfont, bg=self.lf_bg, anchor='w').place(relx=0.05, rely=0.44, relwidth=0.9)
        Label(left_frame, text="Tanggal Lahir", font=labelfont, bg=self.lf_bg, anchor='w').place(relx=0.05, rely=0.57, relwidth=0.9)
        Label(left_frame, text="Jurusan", font=labelfont, bg=self.lf_bg, anchor='w').place(relx=0.05, rely=0.7, relwidth=0.9)
        Entry(left_frame, width=19, textvariable=self.name_strvar, font=entryfont).place(x=20, rely=0.1)
        Entry(left_frame, width=19, textvariable=self.contact_strvar, font=entryfont).place(x=20, rely=0.23)
        Entry(left_frame, width=19, textvariable=self.email_strvar, font=entryfont).place(x=20, rely=0.36)
        Entry(left_frame, width=19, textvariable=self.stream_strvar, font=entryfont).place(x=20, rely=0.75)
        OptionMenu(left_frame, self.gender_strvar, 'Laki-laki', "Perempuan").place(relx=0.05, rely=0.49, relwidth=0.7)
        self.dob = DateEntry(left_frame, font=("Arial", 12), width=15)
        self.dob.place(x=20, rely=0.62)

        Button(left_frame, text='Tambahkan', font=labelfont, command=self.add_record, width=18, bg='#4CAF50', fg='white', relief='groove', borderwidth=6).place(relx=0.025, rely=0.85)

        # Membuat tombol-tombol di frame tengah
        Button(center_frame, text='Hapus Rekaman', font=labelfont, command=self.remove_record, width=15, bg='#f44336', fg='white', relief='groove', borderwidth=6).place(relx=0.1, rely=0.25)
        Button(center_frame, text='Lihat Rekaman', font=labelfont, command=self.view_record, width=15, bg='#2196F3', fg='white', relief='groove', borderwidth=6).place(relx=0.1, rely=0.35)
        Button(center_frame, text='Reset Bidang', font=labelfont, command=self.reset_fields, width=15, bg='#FFEB3B', fg='black', relief='groove', borderwidth=6).place(relx=0.1, rely=0.45)

        # Membuat label untuk daftar mahasiswa di frame kanan
        Label(right_frame, text='Database Mahasiswa', font=headlabelfont, bg='maroon', fg='white').pack(side=TOP, fill=X)
        self.tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                                 columns=("Nama", "Email", "Nomor Kontak", "Jenis Kelamin", "Tanggal Lahir", "Jurusan"))
        X_scroller = Scrollbar(self.tree, orient=HORIZONTAL, command=self.tree.xview)
        Y_scroller = Scrollbar(self.tree, orient=VERTICAL, command=self.tree.yview)
        X_scroller.pack(side=BOTTOM, fill=X)
        Y_scroller.pack(side=RIGHT, fill=Y)
        self.tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
        self.tree.heading('Nama', text='Nama', anchor=CENTER)
        self.tree.heading('Email', text='Email', anchor=CENTER)
        self.tree.heading('Nomor Kontak', text='No Telepon', anchor=CENTER)
        self.tree.heading('Jenis Kelamin', text='Jenis Kelamin', anchor=CENTER)
        self.tree.heading('Tanggal Lahir', text='Tanggal Lahir', anchor=CENTER)
        self.tree.heading('Jurusan', text='Jurusan', anchor=CENTER)
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('#1', width=140, stretch=NO)
        self.tree.column('#2', width=200, stretch=NO)
        self.tree.column('#3', width=80, stretch=NO)
        self.tree.column('#4', width=80, stretch=NO)
        self.tree.column('#5', width=80, stretch=NO)
        self.tree.column('#6', width=150, stretch=NO)
        self.tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
        # Menampilkan rekaman dari database
        self.display_records()

    # Fungsi untuk mengatur ulang bidang input
    def reset_fields(self):
        for i in [self.name_strvar, self.email_strvar, self.contact_strvar, self.gender_strvar, self.stream_strvar]:
            i.set('')
        self.dob.set_date(datetime.datetime.now().date())

# Modul 3 Perulangan (For, While)
# For Loop: Digunakan dalam metode display_records untuk iterasi melalui hasil query database dan menambahkan data ke Treeview.
    # Fungsi untuk menampilkan rekaman dari database ke dalam treeview
    def display_records(self):
        self.tree.delete(*self.tree.get_children())  # Menghapus semua item di treeview
        curr = connector.execute('SELECT NAMA, EMAIL, NO_TELEPON, JENIS_KELAMIN, TGL_LAHIR, JURUSAN FROM MANAJEMEN_MAHASISWA')
        data = curr.fetchall()
        for records in data:  # Menambahkan rekaman ke treeview
            self.tree.insert('', END, values=records)

    # Fungsi untuk menambahkan rekaman baru ke database
    def add_record(self):
        nama = self.name_strvar.get()
        email = self.email_strvar.get()
        kontak = self.contact_strvar.get()
        jenis_kelamin = self.gender_strvar.get()
        tgl_lahir = self.dob.get_date()
        jurusan = self.stream_strvar.get()

# Modul 2 Pengkondisian (If, Else)
# If, Else: Digunakan dalam metode add_record, remove_record, dan view_record untuk validasi input dan pengambilan keputusan berdasarkan kondisi tertentu.        
        # Validasi input pengguna
        if not nama or not email or not kontak or not jenis_kelamin or not tgl_lahir or not jurusan:
            mb.showerror('Kesalahan!', "Harap isi semua bidang yang hilang!")
        else:
            try:
                # Menyimpan data ke database
                connector.execute(
                'INSERT INTO MANAJEMEN_MAHASISWA (NAMA, EMAIL, NO_TELEPON, JENIS_KELAMIN, TGL_LAHIR, JURUSAN) VALUES (?,?,?,?,?,?)', (nama, email, kontak, jenis_kelamin, tgl_lahir, jurusan)
                )
                connector.commit()
                mb.showinfo('Rekaman Ditambahkan', f"Rekaman {nama} berhasil ditambahkan")
                self.reset_fields() # Mengatur ulang bidang input
                self.display_records() # Menampilkan ulang rekaman
            except:
                mb.showerror('Tipe Salah', 'Tipe nilai yang dimasukkan tidak akurat. Harap perhatikan bahwa bidang kontak hanya dapat berisi angka')

    # Fungsi untuk menghapus rekaman dari database
    def remove_record(self):
        if not self.tree.selection():
            mb.showerror('Kesalahan!', 'Silakan pilih item dari database')
        else:
            current_item = self.tree.focus()
            values = self.tree.item(current_item)
            selection = values["values"]
            self.tree.delete(current_item)
            connector.execute('DELETE FROM MANAJEMEN_MAHASISWA WHERE NAMA=? AND EMAIL=?', (selection[0], selection[1]))
            connector.commit()
            mb.showinfo('Selesai', 'Rekaman yang ingin Anda hapus telah berhasil dihapus.')
            self.display_records()

    # Fungsi untuk melihat rekaman yang dipilih
    def view_record(self):
        if not self.tree.selection():
            mb.showerror('Kesalahan!', 'Silakan pilih rekaman untuk dilihat')
        else:
            current_item = self.tree.focus()
            values = self.tree.item(current_item)
            selection = values["values"]

            self.name_strvar.set(selection[0]); self.email_strvar.set(selection[1])
            self.contact_strvar.set(selection[2]); self.gender_strvar.set(selection[3])
            tanggal = datetime.date(int(selection[4][:4]), int(selection[4][5:7]), int(selection[4][8:]))
            self.dob.set_date(tanggal); self.stream_strvar.set(selection[5])

# Menjalankan aplikasi
if __name__ == "__main__":
    root = Tk()
    app = SchoolManagementSystem(root)
    root.mainloop()
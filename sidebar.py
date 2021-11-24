import tkinter as tk
from tkinter import messagebox

from constants import CABANG_KIMIA,FONT_FAMILY
from messenger import messenger

class SideBar(tk.Frame):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)


        # ------ Delete Cabang -------
        self.entry_delete_cabang = tk.Entry(self,width=2, font=(FONT_FAMILY,10))
        self.entry_delete_cabang.place(anchor='n', relx=0.5, rely=0.01,)

        self.btn_delete_cabang = tk.Button(self, 
                command=self.delete_cabang, 
                text="RESET CABANG",
                font=(FONT_FAMILY,10),)
        self.btn_delete_cabang.place(anchor='n', relx=0.5, rely=0.05)
        # ----------------------------

        # ------ Delete ALL Cabang -------
        self.btn_delete_cabang = tk.Button(self, 
                command= lambda: messenger.send("main_app", "reset_cabang()"), 
                text="RESET SEMUA CABANG",
                font=(FONT_FAMILY,10),)
        self.btn_delete_cabang.place(anchor='n', relx=0.5, rely=0.1)
        # ----------------------------

        # ------ INSERT CABANG -------
        self.entry_nomor_cabang = tk.Entry(self,width=2, font=(FONT_FAMILY,10))
        self.entry_nomor_cabang.place(anchor='n', relx=0.2, rely=0.20,)

        self.entry_isi_cabang = tk.Entry(self,width=10, font=(FONT_FAMILY,10))
        self.entry_isi_cabang.place(anchor='n', relx=0.5, rely=0.20,)

        self.btn_insert_cabang = tk.Button(self, 
                command=self.insert_cabang,
                text="INSERT CABANG",
                font=(FONT_FAMILY,10),)
        self.btn_insert_cabang.place(anchor='n', relx=0.5, rely=0.25)
        # ----------------------------

        # ------ HITUNG CABANG -------
        self.btn_calculate = tk.Button(self, command=self.hitung,
           text="JALAN",font=(FONT_FAMILY, 16),)
        self.btn_calculate.place(anchor='n', relx=0.5, rely=0.85,
                                    relwidth=0.8)
        # ----------------------------

    def hitung(self):
        """
        cari tahu nama rantai berdasarkan cabang yang ada
        """
        messenger.send("main_app",
                f"update_nama_rantai()")

    def delete_cabang(self):
        """
        Hapus Cabang ( Balikin cabang ke kondisi awal )
        """
        cabang = self.entry_delete_cabang.get()
        self.entry_delete_cabang.delete(0,'end')

        if cabang == '' or int(cabang) > 6:
            messagebox.showerror("Error","Input Cabang 1-6")
            return

        messenger.send("main_app", f"update_cabang('{cabang}', '{cabang}')")

    def insert_cabang(self):
        """
        Masukkin gugus ke suatu cabang
        """
        nomor_cabang = self.entry_nomor_cabang.get()
        value_cabang = self.entry_isi_cabang.get()
        self.entry_nomor_cabang.delete(0,'end')
        self.entry_isi_cabang.delete(0,'end')

        if nomor_cabang == '' or int(nomor_cabang) > 6:
            messagebox.showerror("Error", "Input Cabang 1-6")
            return

        if value_cabang not in CABANG_KIMIA:
            messagebox.showerror("Error", "Belum bisa pake cabang itu brok...")
            return

        messenger.send("main_app",
                    f"update_cabang('{nomor_cabang}', '{value_cabang}')"
                )


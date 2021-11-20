import tkinter as tk
from tkinter import messagebox

from constants import WINDOW_HEIGHT, BAR_WIDTH, FONT_FAMILY, MESSENGER_CLOCK
from messenger import messenger

class SideBar(tk.Frame):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)


        self.btn_calculate = tk.Button(self, command=self.hitung,
           text="JALAN",font=(FONT_FAMILY, 16),)
        self.btn_calculate.place(anchor='n', relx=0.5, rely=0.85,
                                    relwidth=0.8)


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


    def hitung(self):
        pass

    def delete_cabang(self):
        cabang = self.entry_delete_cabang.get()
        self.entry_delete_cabang.delete(0,'end')

        if cabang == '' or int(cabang) > 6:
            messagebox.showerror("Error","Input Cabang 1-6")
            return

        messenger.send("main_app", f"update_cabang('{cabang}', '{cabang}')")



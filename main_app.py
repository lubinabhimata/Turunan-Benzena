
import tkinter as tk
import utils

from constants import POLYGON_RADIUS, POLYGON_CENTER, FONT_FAMILY
from messenger import messenger

class MainApp(tk.Frame):
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args, **kwargs)


        self.canvas = tk.Canvas(self,
                #bg=None,
                borderwidth=2,highlightbackground='blue')
        self.canvas.place(relheight=1.0, relwidth=1.0)

        self.create_hexagon(self.canvas)
        self.create_cabang_hexagon()


        self.label_nama_iupac = tk.Label(self.canvas, width=30, text="m-etilbenzena",
                bg='lightblue',
                font=(FONT_FAMILY, 18))
        self.label_nama_iupac.place(anchor='n', relx=0.5, rely=0.80)

        self.label_nama_trivial = tk.Label(self.canvas, width=30, text="toluena",
                bg='lightgreen',
                font=(FONT_FAMILY, 18))
        self.label_nama_trivial.place(anchor='n', relx=0.5, rely=0.85)

    def create_hexagon(self, canvas):
        self.points = utils.get_hexagon_vertices(POLYGON_RADIUS, POLYGON_CENTER)# {{{

        canvas.create_polygon(self.points,
                    outline='#111',
                    fill='#fff',
                    width=2)# }}}

    def create_cabang_hexagon(self):
        font = (FONT_FAMILY,16)# {{{
        label_width_char = 10

        self.cabang = {
            1 : tk.Label( # cabang 1
                    self,font=font, width=label_width_char,text="F",),                               
            2 : tk.Label( # cabang 2                               
                    self,font=font, width=label_width_char,text="Br",
                    anchor='w',),
            3 : tk.Label( # cabang 3
                    self,font=font, width=label_width_char,text="C2H5",
                    anchor='w',),
            4 : tk.Label( # cabang 4
                    self,font=font, width=label_width_char,text="NO2",),
            5 : tk.Label( # cabang 5
                    self,font=font, width=label_width_char,text="CH3",
                    anchor='e',),
            6 : tk.Label( # cabang 6
                    self,font=font, width=label_width_char,text="K2SO4",
                    anchor='e',),
        }# }}}

        self.cabang[1].place(x=self.points[0][0], y=self.points[0][1], anchor="s")
        self.cabang[2].place(x=self.points[1][0], y=self.points[1][1], anchor="sw")
        self.cabang[3].place(x=self.points[2][0], y=self.points[2][1], anchor="nw")
        self.cabang[4].place(x=self.points[3][0], y=self.points[3][1], anchor="n")
        self.cabang[5].place(x=self.points[4][0], y=self.points[4][1], anchor="ne")
        self.cabang[6].place(x=self.points[5][0], y=self.points[5][1], anchor="se")

    def update_cabang(self, cabang: str, value: str):
        """
        Update Nama Cabang
        """
        self.cabang[int(cabang)].config(text=value)

    def update_nama_rantai(self, iupac: str, trivial: str):
        """
        Update Nama Rantai berdasarkan cabang2 yang ada
        """
        self.label_nama_iupac.config(text=iupac)
        self.label_nama_trivial.config(text=trivial)

    def reset_cabang(self):
        """
        Reset Semua Cabang menjadi kondisi semula
        """
        for i in range(1,7):
            self.update_cabang(str(i), str(i))





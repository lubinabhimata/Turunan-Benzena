class Cabang():
    def __init__(self, gugus = None) -> None:

        self.gugus = gugus
        self.occupied = True if self.gugus else False

class Rantai:
    prioritas = {
        # Semakin Besar nilainya, prioritasnya semakin tinggi
        'X' : 0,   # Halida
        'NO2' : 1,
        'R' : 2,    # Alkil
        'NH2' : 3, 
        'OH' : 4,
        'CN' : 5,
        'CHO' : 6,
        'SO3H' : 7,
        'COOH' : 8,
    }

    alkil = (
            "CH3", "Metil",
            "C2H5", "Etil"
        )

    def __init__(self) -> None:
        self.cabang = {
            1 : Cabang(),
            2 : Cabang(),
            3 : Cabang(),
            4 : Cabang(),
            5 : Cabang(),
            6 : Cabang(),
        }

    def identifikasi_posisi(self):
        """
        Identifikasi posisi rantai
        orto -> cabang bersebalahan (1, 2)
        meta -> cabang lompat 1 (1,3)
        para -> cabang lompat 2 ( simetris ) ( 1,4)
        """
        pass

    @property
    def jumlah_cabang(self):
        """
        Hitung jumlah cabang yang terisi dari dict cabang
        """
        count = 0
        for cabang in self.cabang.values():
            if cabang.occupied:
                count += 1

        return count

    @property
    def nama_rantai(self):
        # Monosub
        if self.jumlah_cabang == 1:
            pass

        # Bisub
        elif self.jumlah_cabang == 2:
            pass



if __name__ == '__main__':
    pass


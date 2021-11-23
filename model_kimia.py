class Cabang():
    def __init__(self, gugus = None) -> None:

        self.gugus = gugus

    @property
    def occupied(self):
        return True if self.gugus else False


class Rantai:
    prioritas = {
        # Semakin Besar nilainya, prioritasnya semakin tinggi
        'X'     : 0,  # Halida
        'NO2'   : 1,
        'R'     : 2,  # Alkil
        'NH2'   : 3, 
        'OH'    : 4,
        'CN'    : 5,
        'CHO'   : 6,
        'SO3H'  : 7,
        'COOH'  : 8,
    }
    alkil = (
        "metil", "CH3",
        "etil", "C2H5", "CH3CH2", "CH2CH3"
        "butil",
        "isopropil",
        "pentil",
        "propil",
    )

    gol7 = {
        "Cl"    : "Klorida",
        "Br"    : "Bromida",
        "I"     : "Iodida",
        "F"     : "Flour",
    }

    atom_gugus = {
            #"ALKIL"         : "ALKILbenzena",    # ALKIL nanti diganti sama alkil sesuai
            "hidroksi"      : "Hidroksibenzena",
            "amina"         : "Aminobenzena",
            "karboksilat"   : "Karboksibenzena",
            "etena"         : "Vinilbenzena",
            "aldehid"       : "Aldehidabenzena",
            "metoksi"       : "Metoksibenzena"
    }

    def __init__(self) -> None:
        self.cabang = {
            1 : Cabang(),
            2 : Cabang(),
            3 : Cabang(),
            4 : Cabang(),
            5 : Cabang(),
            6 : Cabang(),
        }

    def identifikasi_posisi(self) -> str:
        """
        Identifikasi posisi rantai
        orto -> cabang bersebalahan (1, 2)
        meta -> cabang lompat 1 (1,3)
        para -> cabang lompat 2 ( simetris ) ( 1,4)

        HANYA BERLAKU UNTUK BISUBSTITUEN
        """
        if self.jumlah_cabang == 2:
            pass

        else:
            return ""

    @property
    def jumlah_cabang(self) -> int:
        """
        Hitung jumlah cabang yang terisi dari dict cabang
        """
        count = 0
        for cabang in self.cabang.values():
            if cabang.occupied:
                count += 1

        return count

    def cabang_aktif(self) -> list[int]:
        """
        CABANG-CABANG YANG ADA ISINYA NOMOR BRP AJA
        """
        hasil = []
        for idx,cabang in self.cabang.items():
            if cabang.occupied:
                hasil.append(idx)

        return hasil


    @property
    def nama_rantai(self):
        cabang_aktif = self.cabang_aktif()

        # Monosub
        if self.jumlah_cabang == 1:
            cabang = self.cabang[cabang_aktif[0]]

            if cabang.gugus in self.alkil:
                nama = f"{cabang.gugus}benzena"

            elif cabang.gugus in self.gol7:
                nama = f"{self.gol7[cabang.gugus]}benzena"

            elif cabang.gugus in self.atom_gugus:
                nama = self.atom_gugus[cabang.gugus.lower()]

            else: nama = None

        # Bisub
        elif self.jumlah_cabang == 2:
            pass

        else:
            return "TIDAK ADA CABANG"

        return nama


if __name__ == '__main__':
    rantai = Rantai()

    rantai.cabang[1].gugus = "metil"
    print(rantai.nama_rantai)

    rantai.cabang[1].gugus = "etil"
    print(rantai.nama_rantai)

    rantai.cabang[1].gugus = "F"
    print(rantai.nama_rantai)

    rantai.cabang[1].gugus = "etena"
    print(rantai.nama_rantai)

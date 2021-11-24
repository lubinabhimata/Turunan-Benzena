
class Cabang():
    def __init__(self, gugus: str = "") -> None:

        self.gugus = gugus

    @property
    def occupied(self):
        return False if self.gugus.isdigit() else True


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
        "Cl"    : "kloro",
        "Br"    : "bromo",
        "I"     : "iodo",
        "F"     : "flouro",
    }

    atom_gugus = {
        #"ALKIL"         : "ALKILbenzena",    # ALKIL nanti diganti sama alkil sesuai
        "hidroksi"      : "hidroksi",
        "amina"         : "amino",
        "karboksilat"   : "karboksi",
        "etena"         : "vinil",
        "aldehid"       : "aldehida",
        "metoksi"       : "metoksi"
    }

    def __init__(self) -> None:
        self.cabang = {
            1 : Cabang(gugus="1"),
            2 : Cabang(gugus="2"),
            3 : Cabang(gugus="3"),
            4 : Cabang(gugus="4"),
            5 : Cabang(gugus="5"),
            6 : Cabang(gugus="6"),
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
            cabang_aktif = self.cabang_aktif
            print(cabang_aktif)
            selisih = abs(cabang_aktif[0] - cabang_aktif[1])

            if selisih == 3:
                return "para"
            elif selisih == 1 or selisih == 5:
                return "orto"

            elif selisih == 2 or selisih == 4:
                return "meta"

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

    @property
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
    def nama_rantai(self) -> str:
        cabang_aktif = self.cabang_aktif

        # Monosub
        if self.jumlah_cabang == 1:
            cabang = self.cabang[cabang_aktif[0]]

            if cabang.gugus in self.alkil:
                nama = f"{cabang.gugus}benzena"

            elif cabang.gugus in self.gol7:
                nama = f"{self.gol7[cabang.gugus]}benzena"

            elif cabang.gugus in self.atom_gugus:
                nama = f"{self.atom_gugus[cabang.gugus]}benzena"

            else: 
                nama = "TIDAK DAPAT NAMA"

        # Bisub
        elif self.jumlah_cabang == 2:
            print("BISUB")
            bentuk = self.identifikasi_posisi()
            print(bentuk)

            nama = "BELUM BISA BISUB"

        else:
            return "TIDAK ADA CABANG"

        return nama


if __name__ == '__main__':
    rantai = Rantai()

    rantai.cabang[2].gugus = "metil"
    print(rantai.nama_rantai)

    rantai.cabang[2].gugus = "hidroksi"
    print(rantai.nama_rantai)

    rantai.cabang[2].gugus = "Cl"
    print(rantai.nama_rantai)

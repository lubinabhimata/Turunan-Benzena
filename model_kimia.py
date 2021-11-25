from utils import multi_key_dict_get

class Cabang():
    def __init__(self, gugus: str = "") -> None:
        self.gugus = gugus

    @property
    def occupied(self):
        return False if self.gugus.isdigit() else True

class Rantai:
 
    prioritas = {
        # Semakin Besar nilainya, prioritasnya semakin tinggi
        ("Cl","Br","I","F")     : 0,    # Halida
        'NO2'                   : 1,    # Nitro
        'R'                     : 2,    # Alkil
        'NH2'                   : 3,    # Amina
        'OH'                    : 4,    # Hidroksi
        'CN'                    : 5,    # Sianida
        'CHO'                   : 6,    # Aldehid
        'SO3H'                  : 7,    # Sulfonat
        'COOH'                  : 8,    # Karboksilat
    }
    alkil = (
        "metil", "CH3",
        "etil", "C2H5", "CH3CH2", "CH2CH3",
        "butil", "C4H9", 
        "pentil", "C5H11",
        "isopropil", "C3H7",
        "propil",
    )

    atom_gugus = {
        # Alkil
        ("metil", "CH3",)                       : "metil",
        ("etil", "C2H5", "CH3CH2", "CH2CH3",)   : "etil",
        ("butil", "C4H9")                       : "butil",
        ("pentil", "C5H11")                     : "pentil",
        ("isopropil", "C3H7")                   : "isopropil",
        ("propil", )                            : "propil",

        # Atom Gugus
        ("hidroksi", "OH")                      : "hidroksi",
        ("amina", "NH2")                        : "amino",
        ("karboksilat", "COOH")                 : "karboksi",
        ("etena", "CH2=CH2", "CHCH",)             : "vinil",
        ("aldehid","CHO")                       : "aldehida",
        ("metoksi" "OCH3",)                     : "metoksi",

        # Golongan 7 Halida
        "Cl"                                    : "kloro",
        "Br"                                    : "bromo",
        "I"                                     : "iodo",
        "F"                                     : "flouro",

        # senyawa dari prioritas / random?
        ("nitro", "NO2")                        : "nitro",
        ("sianida", "CN")                       : "siano",
        ("sulfonat", "SO3H")                    : "sulfo",
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
            cabang = self.cabang[cabang_aktif[0]].gugus

            nama = f"{multi_key_dict_get(self.atom_gugus, cabang)}benzena"

        # Bisub
        elif self.jumlah_cabang == 2:
            bentuk = self.identifikasi_posisi()

            cabang_1, cabang_2 = [self.cabang[x].gugus for x in self.cabang_aktif]

            # Cabang Sama
            if (multi_key_dict_get(self.atom_gugus, cabang_1) == 
                    multi_key_dict_get(self.atom_gugus, cabang_2)):
                nama = f"{bentuk}-di{multi_key_dict_get(self.atom_gugus,cabang_1)}benzena"

            # Cabang Beda
            else:

                # Kalo cabang adalah alkil, pembandingnya adalah 'R'
                pembanding_1 = 'R' if cabang_1 in self.alkil else cabang_1
                pembanding_2 = 'R' if cabang_2 in self.alkil else cabang_2


                # Kalo prioritas lebih tinggi, artinya dia jadi cabang prioritas
                if (multi_key_dict_get(self.prioritas,pembanding_1) > 
                        multi_key_dict_get(self.prioritas,pembanding_2)):
                    cabang_prioritas, cabang_bawaan = cabang_1, cabang_2

                else:
                    cabang_prioritas, cabang_bawaan = cabang_2, cabang_1

                nama = (f"{bentuk}-"
                    f"{multi_key_dict_get(self.atom_gugus, cabang_bawaan)}"
                    f"{multi_key_dict_get(self.atom_gugus, cabang_prioritas)}"
                    "benzena"
                )

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

import math

def get_hexagon_vertices(radius , center: tuple):
    """
    MENENTUKAN KOORDINAT DARI SEGI ENAM BERDASARKAN RADIUS DAN TITIK PUSAT

    URUTAN DIMULAI DARI 
        ATAS, KANAN ATAS, KANAN BAWAH, BAWAH, KIRI BAWAH, KIRI ATAS 
    """
    center_x, center_y = center

    x_length = radius * math.cos(math.pi / 6)

    x_vert = (center_x - x_length, center_x, center_x + x_length)
    y_vert = (center_y - radius, center_y - radius/2 , center_y + radius/2, center_y + radius )

    points = [
            (x_vert[1], y_vert[0]), # Tengah ATAS
            (x_vert[2], y_vert[1]), # Kanan Atas
            (x_vert[2], y_vert[2]), # Kanan Bawah
                                 
            (x_vert[1], y_vert[3]), # Tengah Bawah
            (x_vert[0], y_vert[2]), # Kiri Bawah
            (x_vert[0], y_vert[1]), # Kiri Atas
            ]

    return points

if __name__ == '__main__':
    get_hexagon_vertices(50, (100,100))

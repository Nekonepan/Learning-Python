class Titik:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __repr__(self):
        return f"Titik({self._x}, {self._y})"

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_xy(self, x, y):
        self._x = x
        self._y = y


class Titik3D(Titik):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self._z = z

    def __repr__(self):
        return f"Titik3D({self._x}, {self._y}, {self._z})"

    def geser(self, dx=0, dy=0, dz=0):
        """Geser titik 3D sebesar dx, dy, dz"""
        self._x += dx
        self._y += dy
        self._z += dz

    def cermin_sumbu_x(self):
        self._x = -self._x

    def cermin_sumbu_y(self):
        self._y = -self._y

    def cermin_sumbu_z(self):
        self._z = -self._z

    def skala(self, faktor):
        """Perbesar atau perkecil posisi titik dengan faktor tertentu"""
        self._x *= faktor
        self._y *= faktor
        self._z *= faktor


# --- PROGRAM UTAMA ---
if __name__ == "__main__":
    titik_a = Titik3D(1, 2, 3)
    print("Posisi awal:", titik_a)

    titik_a.geser(3, -2, 4)
    print("Setelah digeser:", titik_a)

    titik_a.cermin_sumbu_x()
    print("Setelah dicerminkan terhadap sumbu X:", titik_a)

    titik_a.cermin_sumbu_y()
    print("Setelah dicerminkan terhadap sumbu Y:", titik_a)

    titik_a.cermin_sumbu_z()
    print("Setelah dicerminkan terhadap sumbu Z:", titik_a)

    titik_a.skala(2)
    print("Setelah diskalakan 2x:", titik_a)

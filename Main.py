import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView

taille_icone = 25
p = Path()


class Modele:
    def __init__(self):
        self.DO_VINOS = {
            "Alicante": ((38.3436365, -0.4881708), "Tinto"),
            "Calatayud": ((41.3527628, -1.6422977), "Tinto"),
            "Cariñena": ((41.3382122, -1.2263149), "Tinto"),
            "Condado de Huelva": ((37.3382055, -6.5384658), "Blanco"),
            "Jumilla": ((38.4735408, -1.3285417), "Tinto"),
            "La Gomera": ((28.116, -17.248), "Blanco"),
            "Málaga": ((36.7213028, -4.4216366), "Blanco"),
            "Rías Baixas": ((42.459627886165265, -8.722862824636783), "Blanco"),
            "Ribera del Duero": ((41.49232, -3.005), "Tinto"),
            "Rioja": ((42.29993373411561, -2.486288477690506), "Tinto"),
            "Rueda": ((41.4129785, -4.9597533), "Blanco"),
            "Somontano": ((42.0883878, 0.0994041), "Tinto"),
            "Tarragona": ((41.1172364, 1.2546057), "Tinto"),
            "Txakoli de Getaria": ((43.29428414467608, -2.202397625912913), "Blanco"),
            "Xérès": ((36.6816936, -6.1377402), "Blanco")
        }


class View:
    def __init__(self, fen, control):
        self.fen = fen
        self.control = control
        self.fen.geometry(f"800x600")
        self.fen.title("Vinos Ibericos")
        self.fen.resizable(False, False)
        self.taille_icone = 25
        self.bg = ImageTk.PhotoImage(Image.open(p / "images" / "th.jpg"))
        self.label1 = tk.Label(self.fen, image=self.bg)
        self.blanco = ImageTk.PhotoImage(
            Image.open(p / "images" / "blanco.ico").resize((taille_icone, taille_icone)))
        self.tinto = ImageTk.PhotoImage(
            Image.open(p / "images" / "tinto.ico").resize((taille_icone, taille_icone)))
        self.frame1 = tk.Frame(self.fen, height=600, width=600, highlightbackground="red", highlightthickness=5)
        self.carte = TkinterMapView(self.frame1, width=600, height=600, corner_radius=0, bg_color="purple", max_zoom=7)
        self.frame_button = tk.Frame(self.fen, height=600, width=100, bd=0, highlightthickness=0, bg="#83a6a2")
        self.liste_boutons = []
        self.create_wines_button()
        self.start_position()

    def create_wines_button(self):
        for key, values in Modele().DO_VINOS.items():
            self.liste_boutons.append(
                tk.Button(self.frame_button, text=f"{key}", command=lambda v=values: self.control.place_marker(v)))

    def affichage(self):
        self.label1.place(x=0, y=0)
        for element in self.liste_boutons:
            element.pack()
        self.frame_button.pack(side="left")
        self.frame1.pack(side="left")
        self.carte.pack(fill="both")
        self.fen.mainloop()

    def start_position(self):
        self.carte.set_position(40.4329067, -3.7068316, marker=False)  # Point of view
        self.carte.set_zoom(6)  # zoom of pov


class Controlleur:
    def __init__(self, fen):
        self.vue = View(fen, self)
        self.fen = fen
        self.modele = Modele()

    def center_view(self, carte_position):
        self.vue.carte.set_position(carte_position[0], carte_position[1], marker=False)
        self.vue.carte.set_zoom(6)

    def place_marker(self, valeur):
        self.vue.carte.delete_all_marker()
        icone_a_changer = self.vue.tinto if valeur[1] == "Tinto" else self.vue.blanco
        self.vue.carte.set_marker(valeur[0][0], valeur[0][1], icon=icone_a_changer)
        self.center_view([valeur[0][0], valeur[0][1]])


def main():
    fen = tk.Tk()
    control = Controlleur(fen)
    control.vue.affichage()


if __name__ == "__main__":
    main()

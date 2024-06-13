import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView

DO_VINOS = {
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

taille_icone = 25
p = Path()
fen = tk.Tk()

import tkinter as tk
fen = tk.Tk()

class View():
    def __init__(self, h_w_size):
        self.geometry = fen.geometry(f"{h_w_size}x{h_w_size}")
        # self.title = fen.title("Vinos Ibericos")
        # self.resizable(False, False)
        self.taille = str(h_w_size)
        self.taille_icone = 25

    def affichage(self):
        self.geometry(f"{self.taille}x{self.taille}")
        self.mainloop()

ecran = View(800)

if __name__ == "__main__":
    ecran.affichage()


blanco = ImageTk.PhotoImage(
    Image.open(p / "images" / "blanco.ico").resize((taille_icone, taille_icone)))
tinto = ImageTk.PhotoImage(
    Image.open(p / "images" / "tinto.ico").resize((taille_icone, taille_icone)))
bg = ImageTk.PhotoImage(
    Image.open(p / "images" / "th.jpg"))

label1 = tk.Label(fen, image=bg)
label1.place(x=0, y=0)
frame1 = tk.Frame(fen, height=600, width=600, highlightbackground="red", highlightthickness=5)
frame1.pack()
carte = TkinterMapView(frame1, width=600, height=600, corner_radius=0, bg_color="purple", max_zoom=7)
carte.pack(fill="both")
bouton1 = tk.Button(fen, text="Vin")  # , command=pass)
bouton1.pack()

for key, values in DO_VINOS.items():
    icone_a_changer = tinto if values[1] == "Tinto" else blanco
    carte.set_marker(values[0][0], values[0][1], icon=icone_a_changer)  # repeat as long as wines

carte.set_position(41.6084332, -1.9271726, marker=False)  # Point of view
carte.set_zoom(7)  # zoom of pov

fen.geometry("800x800")
fen.title("Vinos Ibericos")
fen.resizable(False, False)
fen.mainloop()


def centrer_vue(nom_vin, carte_position):
    carte.set_position(carte_position[0], carte_position[1], marker=False)
    carte.set_zoom(7)

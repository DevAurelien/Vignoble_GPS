import position
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView

taille_icone = 50
p = Path()
fen = tk.Tk()

carte = TkinterMapView(fen, width=800, height=800, corner_radius=15)
carte.pack(fill="both")

blanco = ImageTk.PhotoImage(
    Image.open(p / "images" / "blanco.ico").resize((taille_icone, taille_icone)))
tinto = ImageTk.PhotoImage(
    Image.open(p / "images" / "tinto.ico").resize((taille_icone, taille_icone)))

carte.set_marker(38.3436365, -0.4881708, icon=blanco)  # repeat as long as wines
carte.set_position(41.0722841, -3.2523380, marker=False)  # Point of view
carte.set_zoom(7)  # zoom of pov
# carte.set_position(41.3527628, -1.6422977, marker=True)


fen.geometry("800x800")
fen.title("Vinos Ibericos")
fen.resizable(False, False)
fen.mainloop()

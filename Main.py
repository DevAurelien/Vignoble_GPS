import position
import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView

taille_icone = 25
p = Path()
fen = tk.Tk()

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

for key, values in position.DO_VINOS.items():
    icone_a_changer = tinto if values[1] == "Tinto" else blanco
    carte.set_marker(values[0][0], values[0][1], icon=icone_a_changer)  # repeat as long as wines

carte.set_position(41.6084332, -1.9271726, marker=False)  # Point of view
carte.set_zoom(7)  # zoom of pov

fen.geometry("800x800")
fen.title("Vinos Ibericos")
fen.resizable(False, False)
fen.mainloop()

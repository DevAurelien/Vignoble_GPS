import position
import tkinter as tk
from tkintermapview import TkinterMapView

fen = tk.Tk()

carte = TkinterMapView(fen,width=800,height=800)
carte.pack(fill="both")

carte.set_marker(38.3436365,  -0.4881708)
carte.set_position(41.1245119,-2.2380501, marker=False)
carte.set_zoom(7)
# carte.set_position(41.3527628, -1.6422977, marker=True)


fen.geometry("800x800")
fen.title("Vinos Ibericos")
fen.resizable(False, False)
fen.mainloop()

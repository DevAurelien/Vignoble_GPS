import tkinter as tk
import tkinter.messagebox
from pathlib import Path
from PIL import Image, ImageTk
from tkintermapview import TkinterMapView

taille_icone = 25
p = Path()


class Modele:
    def __init__(self):
        self.DO_VINOS = {
            "Alicante": ((38.3436365, -0.4881708), "Tinto",
                         "Alicante (DO) est une appellation d'origine contrôlée espagnole de vins de la région d'Alicante. Elle se divise en deux sous-zones: La Marina, sur la côte nord d'Alicante, et celle du Vinalopó, qui s'étend jusqu'aux limites de Castille-La Manche et Murcie, sur 14 256 ha. Il y a 50 caves inscrites."),
            "Calatayud": ((41.3527628, -1.6422977), "Tinto",
                          "Le Calatayud est un vin d'Espagne à d'appellation d'origine protégée. La zone de production se trouve à l'ouest de la province de Saragosse, formée par 46 municipalités dont le chef lieu est la ville de Calatayud où se trouve le conseil régulateur du vin."),
            "Cariñena": ((41.3382122, -1.2263149), "Tinto",
                         "Le Cariñena est un vin réglé par l'AOC (Denominación de Origen) produit dans la province de Saragosse. Sa création date de 1933 et son centre est la ville de Cariñena. C'est l'AOC doyenne de la Communauté autonome d'Aragon, et l'une des plus anciennes d'Espagne. Située à 50 kilomètres de Saragosse, au sud de l'Ebre, dans la comarque du Campo de Cariñena, encadrée au sud par la Sierra Virgen et à l'ouest par la région vinicole de la DO de Calatayud."),
            "Condado de Huelva": ((37.3382055, -6.5384658), "Blanco",
                                  "Le condado de Huelva est un vin espagnol. Produit dans le vignoble d'Andalousie, il bénéficie d'une dénomination d'origine depuis 1963"),
            "Jumilla": ((38.4735408, -1.3285417), "Tinto",
                        "Jumilla est une dénomination d'origine protégée (DOP) espagnole (équivalent espagnol de l'A.O.C appellation d'origine contrôlée) créée en 1966. Son règlement actuel a été approuvé par ordonnance le 10 novembre 1995 et modifié par ordonnance le 18 avril 2001."),
            "La Gomera": ((28.116, -17.248), "Blanco",
                          "L'appellation La Gomera DO est réservée au vin, au vin de liqueur, au vin mousseux et au vin de raisins surmûris élaborés dans l'appellation qui se situe sur l'île de la Gomera dans l'archipel des Canaries."),
            "Málaga": ((36.7213028, -4.4216366), "Blanco",
                       "Le malaga est un vin doux naturel ou liquoreux élaboré dans la région de Malaga. Ce vin est classé en Denominación de Origen (DO) depuis 1973."),
            "Rías Baixas": ((42.459627886165265, -8.722862824636783), "Blanco",
                            "Les Rias Baixas sont une dénomination d'origine espagnole dont les vins sont produits en Galice dans le secteur des Rías Baixas dans la province de Pontevedra et analysé par Silvia Gago Mariño."),
            "Ribera del Duero": ((41.49232, -3.005), "Tinto",
                                 "Cette comarque produit des vins de grande qualité sous l'AOC Ribera del Duero, qui est aussi étendu à des communes des provinces de Soria, de Ségovie et de Valladolid. Le Conseil Régulateur se trouve à Roa."),
            "Rioja": ((42.29993373411561, -2.486288477690506), "Tinto",
                      "On y produit le vin star de l'Espagne, celui qui a sorti la viticulture ibérique de sa production de masse. Ici, le rendement est le plus faible du pays et le vignoble de la Rioja est le seul, avec le Priorat, à jouir de la distinction D.O.Ca. (vins à appellation d'origine qualifiée, plus rigoureuse que les vins à appellation d'origine contrôlée)."),
            "Rueda": ((41.4129785, -4.9597533), "Blanco",
                      "C'est un vin DO (AOC) Rueda, obtenu à partir de cépages Verdejo à 85 % minimum, Palomino, Viura et Sauvignon blanc. Ce vin est vinifié en vin blanc sec."),
            "Somontano": ((42.0883878, 0.0994041), "Tinto",
                          "Le somontano est un vin d'Espagne d'appellation d'origine contrôlée, produit dans la province de Huesca. La zone vinicole du Somontano se trouve dans la comarca du même nom, dont le chef-lieu est Barbastro. Zone verte au relief abrupt, la vigne se cultive sur les terrasses des vallées qui versent au Nord de la dépression de l'Èbre."),
            "Tarragona": ((41.1172364, 1.2546057), "Tinto",
                          "Le tarragona est un vin espagnol bénéficiant d'une dénomination d'origine.Il appartient au vignoble de Catalogne et est situé dans la province de Tarragone."),
            "Txakoli de Getaria": ((43.29428414467608, -2.202397625912913), "Blanco",
                                   "Cette appellation d'origine certifie l'origine et la culture des raisins utilisés pour le Txakoli, produit dans la région de Getaria et des alentours. Avec son goût légèrement acidulé et ses arômes pleins de fraicheur, il est le vin blanc idéal à déguster l'été accompagné de quelques pintxo. "),
            "Xérès": ((36.6816936, -6.1377402), "Blanco",
                      "Les xérès1 (prononcé [ke.ʁɛs] ou [xe.ʁɛs] dans la langue soutenue, [kse.ʁɛs] ou [gze.ʁɛs] dans la langue courante ; de l’espagnol jerez)2 sont des vins blancs de Denominación de Origen (DO), produits à Jerez de la Frontera, dans le sud de l'Andalousie, en Espagne.")
        }


class View:
    def __init__(self, fen, control):
        self.fen = fen
        self.control = control
        self.fen.geometry(f"800x600")
        self.fen.title("Vinos Ibericos")
        self.fen.resizable(False, False)
        self.taille_icone = 100
        self.bg = ImageTk.PhotoImage(Image.open(p / "images" / "th.jpg"))
        self.label1 = tk.Label(self.fen, image=self.bg)
        self.blanco = ImageTk.PhotoImage(
            Image.open(p / "images" / "blanco.ico").resize((taille_icone * 2, taille_icone * 2)))
        self.tinto = ImageTk.PhotoImage(
            Image.open(p / "images" / "tinto.ico").resize((taille_icone * 2, taille_icone * 2)))
        self.frame1 = tk.Frame(self.fen, height=600, width=600, highlightbackground="red", highlightthickness=5)
        self.carte = TkinterMapView(self.frame1, width=600, height=600, corner_radius=0, bg_color="purple", max_zoom=7)
        self.frame_button = tk.Frame(self.fen, height=600, width=100, bd=0, highlightthickness=0, bg="#83a6a2")
        self.liste_boutons = []
        self.create_wines_button()
        self.start_position()

    def create_wines_button(self):
        for key, values in Modele().DO_VINOS.items():
            self.liste_boutons.append(
                tk.Button(self.frame_button, text=f"{key}", command=lambda v=values: self.control.place_marker(v),
                          bg="#AC1E44" if values[1] == "Tinto" else "#FEEFC5"))

    def affichage(self):
        self.label1.place(x=0, y=0)
        for element in self.liste_boutons:
            element.pack(fill="both", padx=20, pady=2)
        self.frame_button.pack(side="left")
        self.frame1.pack(side="left")
        self.carte.pack(fill="both")
        self.fen.mainloop()

    def start_position(self):
        self.carte.set_position(40.4329067, -3.7068316, marker=False)  # Point of view
        self.carte.set_zoom(6)  # zoom of pov

    def boite_message(self, fen, valeur):
        fen_boite = tk.Toplevel(fen)
        for key, values in Modele().DO_VINOS.items():
            if values[0] == valeur[0]: fen_boite.title(f"{key}")
        fen_boite.geometry(f"300x250+{fen.winfo_x()}+{fen.winfo_y()}")
        tk.Label(fen_boite, text=valeur[2], wraplength=290).pack(padx=5, pady=5)
        tk.Button(fen_boite, text="Parfait", command=fen_boite.destroy, width=50).pack(padx=50, pady=40)


class Controlleur:
    def __init__(self, fen):
        self.vue = View(fen, self)
        self.fen = fen
        self.modele = Modele()

    def center_view(self, carte_position):
        self.vue.carte.set_position(carte_position[0], carte_position[1])

    def place_marker(self, valeur):
        self.vue.carte.delete_all_marker()
        icone_a_changer = self.vue.tinto if valeur[1] == "Tinto" else self.vue.blanco
        self.vue.carte.set_marker(valeur[0][0], valeur[0][1], icon=icone_a_changer)
        self.center_view([valeur[0][0], valeur[0][1]])
        self.info_region(valeur)

    def info_region(self, valeur):
        nom_du_vin = "Vin Blanc" if valeur[1] == "Blanco" else "Vin Rouge"
        # tkinter.messagebox.showinfo(title=f"{nom_du_vin}", message=f"{valeur[0][0]}, {valeur[0][1]}", command=messagebox, width = 7)
        self.vue.boite_message(self.fen, valeur)


def main():
    fen = tk.Tk()
    control = Controlleur(fen)
    control.vue.affichage()


if __name__ == "__main__":
    main()

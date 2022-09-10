import random 
import tkinter as tk


class Personnage:
    def __init__(self, nom, cat):
        self.nom = nom
        self.pv = 20
        self.xp = 1
        self.cat = cat

        if cat == "guerrier":
            self.inv = ["épée,", "potion"]
            
        elif cat == "magicien":
            self.inv = ["batonnet de glace,", "potion"]
            
        elif cat == "voleur":
            self.inv = ["dague rouillé,", "potion"]
            
        elif cat == "elfe":
            self.inv = ["arc en ébène,", "potion"]
            
        elif cat == "orc":
            self.inv = ["hache,", "sang de sanglier"]

        elif cat == "nain":
            self.inv = ["marteau,", "gnole"]
            
        else:
            return print("Veuillez recréer un personnage avec des catégories existantes")
        
    def affiche_caracteristique(self):
        '''affiche les caractéristique'''
        return(" Vôtre personnage s'appelle {}, il possède: {} pv, à {} xp. Il s'agit d'un {} et possède {}.".format(self.nom, self.pv, self.xp, self.cat, self.inv))
        
    def affiche_inventaire(self):
        '''Affiche l'inventaire du personnage'''
        return("Voici l'inventaire: {}.".format(self.inv))
        
        
    def jet_attaque(self):
        '''Renvoie le jet d'attaque'''
        dé = random.randint(1, 20)
        if self.cat == "guerrier":
            return dé + self.xp * 10
            
        elif self.cat == "magicien":
            return dé + self.xp * 10
            
        elif self.cat == "voleur":
            return dé + self.xp * 3
            
        elif self.cat == "elfe":
            return dé + self.xp * 8
        
        elif self.cat == "orc":
            return dé + self.xp * 4
        
        elif self.cat == "nain":
            return dé + self.xp * 10.5
    
    def jet_defence(self):
        '''Renvoie le jet de defence'''
        dé = random.randint(1, 20)
        if self.cat == "guerrier":
            return dé + self.xp * 8
            
        elif self.cat == "magicien":
            return dé + self.xp * 7
            
        elif self.cat == "voleur":
            return dé + self.xp * 9
            
        elif self.cat == "elfe":
            return dé + self.xp * 10
        
        elif self.cat == "orc":
            return dé + self.xp * 15
        
        elif self.cat == "nain":
            return dé + self.xp * 9
   
        
    def change_pdv(self, nb_pdv):
        '''change les pv du perso'''
        self.pv += nb_pdv
        
    def change_xp(self, nb_xp):
        '''change l'xp du perso'''
        self.xp += nb_xp

def jeu():
    '''lance le combat'''
    j1 = Personnage(str(j1nom_input.get()), str(j1classe_input.get()))                
    j2 = Personnage(str(j2nom_input.get()), str(j2classe_input.get()))
    pvj1a.configure(text=j1.pv)
    invj1a.configure(text=j1.inv)
    pvj2a.configure(text=j2.pv)
    invj2a.configure(text=j2.inv)
    statj1.configure(text=j1.affiche_caracteristique)
    statj2.configure(text=j2.affiche_caracteristique)
    perso=0
    if perso == 0:
        tour = 1
        while j1.pv > 0 and j2.pv > 0:
            if j1.pv < 10:
                if j1.inv[1] == "potion" or j1.inv[1] == "gnole" or j1.inv[1] == "sang de sanglier":
                   j1.change_pdv(random.randint(5, 10))
            if j2.pv < 10:
                if j2.inv[1] == "potion" or j2.inv[1] == "gnole" or j2.inv[1] == "sang de sanglier":
                   j2.change_pdv(random.randint(5, 10))            
            if tour == 1:
                tour = 2
                degat = j1.jet_attaque()
                defen = j2.jet_defence()
                if degat > defen:
                    j2.change_pdv(random.randint(-8, -1))
                    pvj2a.configure(text=j2.pv)
                    pvj1a.configure(text=j1.pv)
                else:
                    j1.change_pdv(random.randint(-4, -1))
                    pvj2a.configure(text=j2.pv)
                    pvj1a.configure(text=j1.pv)
            if tour == 2:
                tour = 1
                degat = j2.jet_attaque()
                defen = j1.jet_defence()
                if degat > defen:
                    j1.change_pdv(random.randint(-8, -1))
                    pvj2a.configure(text=j2.pv)
                    pvj1a.configure(text=j1.pv)
                else:
                    j2.change_pdv(random.randint(-4, -1))
                    pvj2a.configure(text=j2.pv)
                    pvj1a.configure(text=j1.pv)
        if j1.pv < j2.pv:
            vainqueura.configure(text=j2.nom)
        else:
            vainqueura.configure(text=j1.nom)



Jeu = tk.Tk()

Jeu.title('Simulateur de combat')
Jeu.geometry("1700x900")
Jeu.configure(bg='#008000')


Intro = tk.Label(Jeu, text="Cette interface graphique a pour but de simuler un combat entre deux personnages, Joueur 1 et Joueur 2. Vous pouvez choisir entre six classes: guerrier, magicien, voleur, orc, nain et elfe.", bg='#008000')
Intro.grid(column = 0, columnspan = 3, pady=30, padx=30)
# frame 1

Joueur1 = tk.Frame(Jeu, borderwidth=2, bg='#800000')
Joueur1.grid(column = 0, row=2)

jo1 = tk.Label(Joueur1, text="Joueur1", bg='#800000')
jo1.grid(row=0, column=1)

#mise en place nom j1
j1nom = tk.Label(Joueur1, text="Inscrire le nom", bg='#800000')
j1nom.grid(row=1, column=0)
j1nom_input = tk.Entry(Joueur1, bg='#808000')
j1nom_input.grid(row=1, column=1)

#mise en place classe j1
j1classe = tk.Label(Joueur1, text="Inscrire la classe", bg='#800000')
j1classe.grid(row=2, column=0)
j1classe_input = tk.Entry(Joueur1, bg='#808000')
j1classe_input.grid(row=2, column=1)

#affichage pv j1
pvj1 = tk.Label(Joueur1, text="Points de vie", bg='#800000')
pvj1.grid(row=3, column=0)
pvj1a = tk.Label(Joueur1, text="'Ce message sera remplacé par les pv'", bg='#808000')
pvj1a.grid(row=3, column=1)

#affichage inv

invj1 = tk.Label(Joueur1, text="Inventaire", bg='#800000')
invj1.grid(row=4, column=0)
invj1a = tk.Label(Joueur1, text="'Ce message sera remplacé par l'inventaire'", bg='#808000')
invj1a.grid(row=4, column=1)



# frame 3
Joueur2 = tk.Frame(Jeu, borderwidth=2, bg='#800000')
Joueur2.grid(column = 3, row=2)

jo2 = tk.Label(Joueur2, text="Joueur2", bg='#800000')
jo2.grid(row=0, column=1)

#mise en place nom j2
j2nom = tk.Label(Joueur2, text="Inscrire le nom", bg='#800000')
j2nom.grid(row=1, column=0)
j2nom_input = tk.Entry(Joueur2, bg='#808000')
j2nom_input.grid(row=1, column=1)

#mise en place classe j2
j2classe = tk.Label(Joueur2, text="Inscrire la classe", bg='#800000')
j2classe.grid(row=2, column=0)
j2classe_input = tk.Entry(Joueur2, bg='#808000')
j2classe_input.grid(row=2, column=1)

#affichage pv j2
pvj2 = tk.Label(Joueur2, text="Points de vie", bg='#800000')
pvj2.grid(row=3, column=0)
pvj2a = tk.Label(Joueur2, text="'Ce message sera remplacé par les pv'", bg='#808000')
pvj2a.grid(row=3, column=1)

#affichage inv j2

invj2 = tk.Label(Joueur2, text="Inventaire", bg='#800000')
invj2.grid(row=4, column=0)
invj2a = tk.Label(Joueur2, text="'Ce message sera remplacé par l'inventaire'", bg='#808000')
invj2a.grid(row=4, column=1)


vainqueur = tk.Label(Jeu, text="Le vainqueur est :", bg='#800000')
vainqueur.grid(row=5, column=0)
vainqueura = tk.Label(Jeu, text="message remplacé par vainqueur", bg='#800000')
vainqueura.grid(row=5, column= 1)

launch_button = tk.Button(Jeu, text="Lancer le test", command=jeu, bg="#FF0000")
launch_button.grid(row = 3, columnspan=5)




#### Affiche l'arene ici 
# frame 2
# arene = tk.Frame(Jeu, borderwidth=2)
# arene.grid(column = 0, columnspan = 3)
# photo = tk.PhotoImage(file="arene.png")
# canvas = tk.Canvas(arene,width=2000, height=920)
# canvas.create_image(0, 0, image=photo)
# canvas.grid()




statj1 = tk.Label(Jeu, text="statistiques joueur1", bg='#008080')
statj1.grid(row=6, column=0, pady=20)
statj2 = tk.Label(Jeu, text="statistiques joueur2", bg='#008080')
statj2.grid(row=7, column= 0, pady=20)


Jeu.mainloop()
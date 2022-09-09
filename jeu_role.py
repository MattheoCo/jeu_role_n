import random 

class Personnage:
    def __init__(self, nom, cat):
        self.nom = nom
        self.pv = 20
        self.xp = 1
        self.cat = cat

        if cat == "guerrier":
            self.inv = ["épée", "potion"]
            
        elif cat == "magicien":
            self.inv = ["batonnet de glace", "potion"]
            
        elif cat == "voleur":
            self.inv = ["dague rouillé", "potion"]
            
        elif cat == "elfe":
            self.inv = ["arc en ébène", "potion"]
            
        else:
            return print("Veuillez recréer un personnage avec des catégories existantes")
        
    def affiche_caracteristique(self):
        '''affiche les caractéristique'''
        print(" Vôtre personnage s'appelle {}, il possède: {} pv, à {} xp. Il s'agit d'un {} et possède {}.".format(self.nom, self.pv, self.xp, self.cat, self.inv))
        
    def affiche_inventaire(self):
        '''Affiche l'inventaire du personnage'''
        print("Voici l'inventaire: {}.".format(self.inv))
        
        
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
   
        
    def change_pdv(self, nb_pdv):
        '''change les pv du perso'''
        self.pv += nb_pdv
        
    def change_xp(self, nb_xp):
        '''change l'xp du perso'''
        self.xp += nb_xp
        
def jeu(j1,j2):
    '''lance le combat'''
    
    perso=0
    if perso == 0:
        tour = 1
        while j1.pv > 0 and j2.pv > 0:
            if tour == 1:
                tour = 2
                degat = j1.jet_attaque()
                defen = j2.jet_defence()
                if degat > defen:
                    j2.change_pdv(random.randint(-8, -1))
                    j1.affiche_caracteristique()
                    j2.affiche_caracteristique()
                else:
                    j1.change_pdv(random.randint(-4, -1))
                    j1.affiche_caracteristique()
                    j2.affiche_caracteristique()
            if tour == 2:
                tour = 1
                degat = j2.jet_attaque()
                defen = j1.jet_defence()
                if degat > defen:
                    j1.change_pdv(random.randint(-8, -1))
                    j1.affiche_caracteristique()
                    j2.affiche_caracteristique()
                else:
                    j2.change_pdv(random.randint(-4, -1))
                    j1.affiche_caracteristique()
                    j2.affiche_caracteristique()    
                    
j1 = Personnage("toto", "guerrier")                
j2 = Personnage("Connan", "guerrier")            
jeu(j1,j2)
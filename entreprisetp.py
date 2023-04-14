import random


class Entreprise:
    def __init__(self, nom, capital):
        self.capital_initial = capital # Capital initial de l'entreprise
        self.nom = nom # Nom de l'entreprise
        self.capital = capital # Capital actuel de l'entreprise
        self.employes = [] # Liste des employés de l'entreprise
        self.matieres_premieres = [] # Liste des matières premières de l'entreprise
        self.materiels = [] # Liste des matériels de l'entreprise
        self.tour = 0 # Compteur de tours
        self.arret_evenements = False # Indicateur d'arrêt des événements
        self.revenu = 0 # Revenu de l'entreprise
        self.machines = [] #Liste des machines achetés
        self.utilisateur = "" #Pseudo des utilisateurs

    def demander_employes(self):
        while True:
            try:
                employes = int(input(f"Combien d'employés avez-vous dans votre entreprise '{self.nom}' ? ")) #On demande a chaque utilisateur d'entrer un nombre en retour
                if employes < 0:
                    raise ValueError("Le nombre d'employés doit être positif.") # Lever une exception pour un nombre d'employés négatif
                break
            except ValueError as e:
                print(f"Erreur : {e}") # Afficher un message d'erreur pour une exception de type ValueError
        self.employes = employes # Affecter le nombre d'employés saisi à la variable self.employes

    def __str__(self):
        return self.nom # Retourner le nom de l'entreprise lorsqu'on convertit l'objet en chaîne de caractères
    
    def demander_utilisateur(self):
        self.utilisateur = input(f"Entrez le nom d'utilisateur qui détient l'entreprise '{self.nom}': ") #On demande a chaque utilisateur d'entrer un pseudo

    def gestion_finances(self):
        # Ajout de la fluctuation des prix des matières premières et de l'énergie
        if self.tour >= 3:
            # Génération aléatoire d'événements
            evenements = ["Fluctuation des prix des matières premières", "Fluctuation des prix de l'énergie", "Concurrence entre entreprises","pandémie","Nouveaux fournisseurs","Nouveaux marchés/débouchés","Publicité"]
            evenement = random.choice(evenements)

            if evenement == "Fluctuation des prix des matières premières":
                self.calcul_fluctuation_prix_matiere_premiere() # Appel d'une méthode pour calculer la fluctuation des prix des matières premières
            elif evenement == "Fluctuation des prix de l'énergie":
                self.calcul_fluctuation_prix_energie() # Appel d'une méthode pour calculer la fluctuation des prix de l'énergie
            elif evenement == "Concurrence entre entreprises":
                self.calcul_concurrence_entreprises() # Appel d'une méthode pour calculer la concurrence entre entreprises
            elif evenement == "pandémie":
                self.calcul_pandémie() # Appel d'une méthode pour calculer l'impact d'une pandémie
            elif evenement == "Concurrence entre entreprises":
                self.calcul_concurrence_entreprises() # Appel d'une méthode pour calculer la concurrence entre entreprises
            elif evenement == "Nouveaux fournisseurs":
                self.calcul_Nouveaux_fournisseurs() # Appel d'une méthode pour gérer l'arrivée de nouveaux fournisseurs
            elif evenement == "Nouveaux marchés/débouchés":
                self.calcul_Nouveaux_marchés_débouchés() # Appel d'une méthode pour gérer l'ouverture de nouveaux marchés/débouchés
            elif evenement == "Publicité":
                self.calcul_Publicité() # Appel d'une méthode pour gérer les dépenses de publicité


        prix_matieres_premieres = 10000 #
        cout_salarie =  self.employes * 10 
        revenu =  self.employes * 100 
        cout_energie_total = self.employes * 4
        self.capital += revenu
        print(self.capital)
        self.capital -=  cout_energie_total + cout_salarie + prix_matieres_premieres

        print(f"Bienvenue : {self.utilisateur}")
        print(f"Salaire total des employés : {revenu}, capital actif : {self.capital}, coût énergie : {cout_energie_total}, coût salarié : {cout_salarie}, coût matières premières : {prix_matieres_premieres}") #affichage résumé de chaque tour

    def calcul_fluctuation_prix_matiere_premiere(self):
        #le calcul associé à "Fluctuation des prix des matières premières"
        montant = random.randint(-10000, -1000)  #montant aléatoire pour l'evenement en question
        self.capital += montant
        print(f"Le prix des matières premières a fluctué, le capital de l'entreprise a été modifié de {montant}.") #Affichage

    def calcul_fluctuation_prix_energie(self):
        #le calcul associé à "Fluctuation des prix de l'énergie"
        montant = random.randint(-5000, -500)  #montant aléatoire pour l'evenement en question
        self.capital += montant
        print(f"Le prix de l'énergie a fluctué, le capital de l'entreprise a été modifié de {montant}.") #Affichage

    def calcul_concurrence_entreprises(self):
        #le calcul associé à "concurrence_entreprises"
        montant = random.randint(-1000, -100)  #montant aléatoire pour l'evenement en question
        self.capital += montant
        print(f"L'analyse de la concurrence des entreprises est rude et a un cout , le capital de l'entreprise a été modifié de {montant}.") #Affichage

    def calcul_pandémie(self):
        #le calcul associé à "pandémie"
        montant = random.randint(-10000, -1000)  #montant aléatoire pour l'evenement en question
        self.capital += montant
        print(f"La pandémie a ralentis l'économie de votre entreprise, le capital de l'entreprise a été modifié de {montant}.") #Affichage

    def calcul_Nouveaux_fournisseurs(self):
        #le calcul associé à "Nouveaux_fournisseurs"
        montant = random.randint(5000, 50000)  #montant aléatoire pour l'evenement en question
        self.capital += montant
        print(f"c'est un investissement qui porte ses fruits pour avoir penser a collaborer avec d'autres fournisseurs, le capital de l'entreprise a été modifié de {montant}.") #Affichage

    def calcul_Nouveaux_marchés_débouchés(self):
        #le calcul associé à "Nouveaux_marchés_débouchés"
        montant = random.randint(100000, 1000000)  #montant aléatoire pour l'evenement en question
        self.capital += montant
        print(f"Vous aimez le gout du risque mais ça paye vous vous etes lancé dans un nouveau marché, le capital de l'entreprise a été modifié de {montant}.") #Affichage
    

    def calcul_Publicité(self):
        #calcul associé à "Publicité"
        montant = random.randint(10000, 100000)  #montant aléatoire pour l'evenement en question
        self.capital += montant
        print(f"C'est une excellente idée de faire de la publicité pour augmenter le chiffre de votre entreprise , le capital de l'entreprise a été modifié de {montant}.") #Affichage

    def investir_ressources(self):
        choix = input("Voulez-vous investir dans : (1) main d'oeuvre, (2) matières premières, ou (3) équipements ? ")
        # Demande à l'utilisateur de choisir entre 3 options : main d'oeuvre, matières premières, ou équipements
        if choix == "1":
            cout = random.randint(500, 5000)
            # Génère un coût aléatoire pour embaucher une nouvelle machine
            if self.capital >= cout:
                self.machines.append("machine")
                self.capital -= cout
                #Condition pour ajouter un nouvel employé à la liste "employes" et déduit le coût du capital
                print("Vous avez acheter une nouvelle machine !") #Affichage 
            else:
                print("Vous n'avez pas assez d'argent pour embaucher une nouvelle machine.") # Affiche un message si l'utilisateur n'a pas suffisamment d'argent pour embaucher un nouvel employé
        elif choix == "2":
            cout = random.randint(100, 1000)
            # Génère un coût aléatoire pour acheter des matières premières
            if self.capital >= cout:
                self.matieres_premieres.append("matière première")
                self.capital -= cout
                # Ajoute des matières premières à la liste "matieres_premieres" et déduit le coût du capital
                print("Vous avez acheté des matières premières !") #Affichage
            else:
                print("Vous n'avez pas assez d'argent pour acheter des matières premières.")
                # Affiche un message si l'utilisateur n'a pas suffisamment d'argent pour acheter des matières premières
        elif choix == "3":
            cout = random.randint(500, 5000)
            # Génère un coût aléatoire pour acheter un nouvel équipement
            if self.capital >= cout:
                self.materiels.append("matériel")
                self.capital -= cout
                # Ajoute un nouvel équipement à la liste "materiels" et déduit le coût du capital
                print("Vous avez acheté un nouvel équipement !") #Affichage
            else:
                print("Vous n'avez pas assez d'argent pour acheter un nouvel équipement.") 
                # Affiche un message si l'utilisateur n'a pas suffisamment d'argent pour acheter un nouvel équipement
        else:
            print("Choix invalide.")
            #affiche un message quand le choix de l'utilisateur ne correspond pas a ce qu'on lui demande

    
    

        
    def tour_suivant(self):
        self.tour += 1  # Incrémentation du tour
        self.capital += self.revenu * 1  # Ajout du revenu au capital
        print(f"Tour {self.tour} - {self.nom}")  # Affichage du tour et du nom de l'entreprise
        self.gestion_finances()  # Appel à une fonction de gestion des finances

        self.investir_ressources()  # Appel à une fonction d'investissement des ressources

        if self.tour <= 15:  # Condition pour vérifier si le tour est inférieur ou égal à 15
            print(f"Tour de l'entreprise - Tour {self.tour}")
        # Reste du code pour le tour suivant
        else:
            print("Fin du jeu. Vous avez atteint le tour 15.")  # Message de fin du jeu



# Demande du nom,du capital,du pseudo et du nombre d'employés de départ pour l'entreprise 1
nom_entreprise1 = input("Entrez le nom de l'entreprise 1 : ")
capital_entreprise1 = int(input("Entrez le capital de départ de l'entreprise 1 : "))
entreprise1 = Entreprise(nom_entreprise1, capital_entreprise1)
entreprise1.demander_utilisateur()

# Demande du nom et du capital,du pseudo et du nombre d'employés de départ pour l'entreprise 2
nom_entreprise2 = input("Entrez le nom de l'entreprise 2 : ")
capital_entreprise2 = int(input("Entrez le capital de départ de l'entreprise 2 : "))
entreprise2 = Entreprise(nom_entreprise2, capital_entreprise2)
entreprise2.demander_utilisateur()

entreprise1.demander_employes()  # Appel à une fonction de demande du nombre d'employés pour l'entreprise 1
entreprise2.demander_employes()  # Appel à une fonction de demande du nombre d'employés pour l'entreprise 2

while True:
    entreprise1.tour_suivant()  # Appel à une fonction pour le tour suivant de l'entreprise 1
    input("Appuyez sur Entrée pour passer au tour de l'entreprise 2.")
    entreprise2.tour_suivant()  # Appel à une fonction pour le tour suivant de l'entreprise 2
    input("Appuyez sur Entrée pour passer au tour de l'entreprise 1.")

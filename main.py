# Librairies 
import json

# Déclarations de variables


quitting_words = ["quit", "Quit", "q", "Q", "ciao", \
                  "bye", "byebye", "au revoir", "over", "quitter", "quitté"]

retrait_words = ["r", "R", "retrait", "RETRAIT", "Retrait"]

depot_words = ["d", "D", "depot", "DEPOT", "Depot"]

solde_words = ["s", "S", "SOLDE", "solde", "Solde"]




# Partie Json
with open("clients.json", "r") as f:
    clients = json.load(f)

def save_clients_dict_in_json_file (clients):
    with open("clients.json", "w") as f:
        json.dump(clients, f, indent=4)

print (clients.keys ())

def is_a_valid_client_id (client_id):
    """
    La fonction permet de vérifier si l'ID client existe (compare parmis la liste ID client récupéré du JSON)
    Entree : Str
    Sortie : Boolen
    """
    return client_id in clients

def is_not_a_valid_client_id (client_id):
    return not is_a_valid_client_id (client_id)

def reask_for_client_id():
     return input ("Ton id client: ")

def ask_for_client_id ():
    client_id = input ("Ton id client: ")
    while is_not_a_valid_client_id (client_id):
        print ("Ton id est invalide, réessaie.")
        client_id = reask_for_client_id ()
    return client_id


# Partie depot
def ask_given_money():
    """Demande le montant à déposer
    Entree : 
    Sortie : Entier (qui a été vérifier)
    """
    montant = input("Combien veux-tu déposer ? ")
    while montant.isdigit() == False :
        print("Veuillez rentrer un montant valide")
        montant = input("Combien veux-tu déposer ? ")

    return int(montant)

def depot(client_id):
    global clients
    """Effectue un dépôt sur le compte du client"""
    montant = ask_given_money()

    clients[client_id]['solde'] += montant
    print(f"Dépôt de {montant} € effectué")
    print(f"Nouveau solde : {clients[client_id]['solde']} €")


    save_clients_dict_in_json_file (clients)

#Partie retrait
def ask_wanted_money():
    """Demande le montant à retirer
    Entree : 
    Sortie : Entier (qui a été vérifier)
    """
    montant = input("Combien veux-tu retirer ? ")
    while montant.isdigit() == False or int(montant)%5 != 0 :
        print("Veuillez rentrer un montant valide")
        montant = input("Combien veux-tu retirer ? ")

    return int(montant)


def decomposer_billet(montant):
    """
    Permet de décomposer le montant retiré en billet, avec une méthode qui économise le nombre de billet à donner
    entree : int montant
    Sortie : liste [nb_billets_50, nb_billets_20, nb_billets_10, nb_billets_5]
    """
    liste_billet = []

    nbr_billet_50 = montant // 50
    montant = montant % 50

    nbr_billet_20 = montant // 20
    montant = montant % 20

    nbr_billet_10 = montant // 10
    montant = montant % 10

    nbr_billet_5 = montant // 5
    montant = montant % 5  

    liste_billet = [nbr_billet_50, nbr_billet_20, nbr_billet_10, nbr_billet_5]
    #print(liste_billet)
    return liste_billet

def retrait(client_id):
    global clients
    """Effectue un retrait sur le compte du client"""
    montant = ask_wanted_money()

    while clients[client_id]['solde'] - montant < 0:
        print("== Le montant n'est pas disponible sur votre compte ==")
        montant = ask_wanted_money()

    clients[client_id]['solde'] -= montant


    print(f"Retrait de {montant} € effectué")
    liste_billet_2 = decomposer_billet(montant)
    print()
    print("== Billets distribués : ==")
    print()
    print(f"{liste_billet_2[0] } billet de 50 €")
    print(f"{liste_billet_2[1] } billet de 20 €")
    print(f"{liste_billet_2[2] } billet de 10 €")
    print(f"{liste_billet_2[3] } billet de 5 €")
    print(f"Nouveau solde : {clients[client_id]['solde']} €")
    print()
    print("== Fin du retrait ==")
    print()

    save_clients_dict_in_json_file (clients)

    

def main():
    """Fonction main qui est appelée au lancement du script et qui appelle les autres fonctions pour réaliser des tâches précises que demande l'utilisateur"""
    print("=========== BIENVENUE - PIOCHE BANQUE [PB] ===========")
    print()
    print("Veuillez vous identifier en rentrant votre ID client (code PIN)")
    client_id = ask_for_client_id ()
    print(f"Bienvenue {clients[client_id]['prenom']} {clients[client_id]['nom']} !")
    print(f"Ton solde est de {clients[client_id]['solde']} €.")

    quitter = False
    while quitter == False:
        print("Veuillez choisir les opérations à effectuer :")
        print()
        print("1 : Retrait")
        print("2 : Dépot")
        print("3 : Consulter le solde")
        print("4 : Quitter la banque")
        print()
        entree = input("Entrez la commande :")
        if entree in quitting_words:
            print("Au revoir.")
            quitter = True
            # fermer le json
        elif entree in retrait_words:
            # Fonction retrait
            retrait(client_id)
        elif entree in depot_words:
            depot(client_id)
            #apelle fonction depot
        elif entree in solde_words:
            print(f"Ton solde est de {clients[client_id]['solde']} €.")
            #Fonction qui donne le solde du client
        else :
            print("Commande non valide")


main()
#Partie retrait

import json 

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

def save_clients_dict_in_json_file (clients):
    with open("clients.json", "w") as f:
        json.dump(clients, f, indent=4)

    save_clients_dict_in_json_file (clients)
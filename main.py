# Librairies 
from json import*

from data import*

# Partie Json

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

from depot import*

from retrait import*
    
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
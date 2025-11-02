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
        clients = json.load(f)

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
    """Demande le montant à déposer"""
    montant = input("Combien veux-tu déposer ? ")
    try:
        montant = float(montant)
        return montant
    except:
        print("Ce n’est pas un nombre valide.")
        return ask_given_money()

def is_a_given_money(montant):
    """Vérifie que le montant est supérieur à 0"""
    return montant > 0

def depot(client_id):
    """Effectue un dépôt sur le compte du client"""
    montant = ask_given_money()
    if not is_a_given_money(montant):
        print("Le montant doit être positif.")
        return

    clients[client_id]['solde'] += montant
    print(f"✅ Dépôt de {montant} € effectué avec succès !")
    print(f"💰 Nouveau solde : {clients[client_id]['solde']} €")

    save_clients_dict_in_json_file(clients)

    

def main():
    """Fonction main qui est appelée au lancement du script et qui appelle les autres fonctions pour réaliser des tâches précises que demande l'utilisateur"""
    print("------------ BIENVENUE - PIOCHE BANQUE PB -------------")
    print("Veuillez vous identifier en rentrant votre ID client (code PIN)")
    client_id = ask_for_client_id ()
    print(f"Bienvenue {clients[client_id]['prenom']} {clients[client_id]['nom']} !")
    print(f"Ton solde est de {clients[client_id]['solde']} €.")

    quitter = False
    while quitter == False:
        print("Veuillez choisir les opérations à effectuer :")
        print("R : retrait")
        print("D : dépot")
        print("S : Consulter le solde")
        print("Q : quitter la banque")
        entree = input("Entrez la commande :")
        if entree in quitting_words:
            print("Au revoir.")
            quitter = True
        elif entree in retrait_words:
            # Fonction retrait
            pass
        elif entree in depot_words:
            #apelle fonction depot
            depot(client_id)
        elif entree in solde_words:
            print(f"Ton solde est de {clients[client_id]['solde']} €.")
        else :
            print("Commande non valide")


main()
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
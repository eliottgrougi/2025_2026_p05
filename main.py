import json

from clients import*
def is_a_valid_client_id (client_id):
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

client_id = ask_for_client_id ()

print(f"Bienvenue {clients[client_id]['prenom']} {clients[client_id]['nom']} !")
print(f"Ton solde est de {clients[client_id]['solde']} €.")
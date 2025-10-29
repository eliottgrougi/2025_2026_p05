
def is_a_valid_client_id (client_id):
    return clients ["client_id"]["nom"]["prenom"]["solde"]

def is_not_a_valid_client_id (client_id):
    return not (is_a_valid_client_id (client_id))

def ask_for_client_id ():
    client_id = input ("Ton id client: ")
    while is_not_a_valid_client_id (client_id):
        reask_for_client_id ()
    return client_id
    print (clients)

def reask_for_client_id():
     client_id = input ("Ton id client: ")
     return client_id
client_id = ask_for_client_id ()
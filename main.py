from clients import*
def is_a_valid_client_id (client_id):
    return client_id in clients

def is_not_a_valid_client_id (client_id):
    return not is_a_valid_client_id (client_id)

def ask_for_client_id ():
    client_id = input ("Ton id client: ")
    while is_not_a_valid_client_id (client_id):
        print ("Ton id est invalide, réessaie.")
        client_id = reask_for_client_id ()
    return client_id

def reask_for_client_id():
     return input ("Ton id client: ")
 
client_id = ask_for_client_id ()
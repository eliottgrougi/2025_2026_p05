import json 

clients = { 
    4593 :{
        "nom":"Delamarre",
         "prénom":"Marc",
         "solde":"50.00"
        } ,
    5623: {
        "nom":"Gabilla",
         "prénom":"Esteban",
         "solde":5.50
        },
    4587: {
        "nom":"Bécaud",
         "prénom":"Raphaël",
         "solde":100.25
         },
    9658: {
        "nom":"Marpung",
        "prénom":"Jensonn",
        "solde":50.00
         }
 }

print (clients.keys ())

def save_clients_dict_in_json_file (clients):
    with open("clients.json", "w") as f:
        json.dump(clients, f, indent=4)

def is_a_valid_client_id (client_id):
    return client_id in clients.keys ()

def is_not_a_valid_client_id (client_id):
    return not (is_a_valid_client_id (client_id))

def ask_for_client_id ():
    client_id = input ("Ton id client: ")
    while is_not_a_valid_client_id (client_id):
        reask_for_client_id ()
    return client_id

def reask_for_client_id():
     client_id = input ("Ton id client: ")
     return client_id
client_id = ask_for_client_id ()



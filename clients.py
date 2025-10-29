import json 

clients = { 
    "4593" :{
        "nom":"Delamarre",
         "prenom":"Marc",
         "solde":150.00
        } ,
    "5623": {
        "nom":"Gabilla",
         "prenom":"Esteban",
         "solde":205.50
        },
    "4587": {
        "nom":"Becaud",
         "prenom":"Raphael",
         "solde":100.25
         },
    "9658": {
        "nom":"Marpung",
        "prenom":"Jensonn",
        "solde":50.00
         }
 }

def save_clients_dict_in_json_file (clients):
    with open("clients.json", "w") as f:
        json.dump(clients, f, indent=4)

print (clients.keys ())


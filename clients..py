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
         "solde":205.50
        },
    4587: {
        "nom":"Bécaud",
         "prénom":"Raphaël",
         "solde":200.25
         },
    9658: {
        "nom":"Marpung",
        "prénom":"Jensonn",
        "solde":50.00
         }
 }

print (clients.keys ())

with open("clients.json", "w") as f:
    json.dump(clients, f, indent=4)

# print (get_client ("Bécaud"))


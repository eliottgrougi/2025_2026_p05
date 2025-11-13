import json

quitting_words = ["quit", "Quit", "q", "Q", "ciao", \
                  "bye", "byebye", "au revoir", "over", "quitter", "quitté", "4"]

retrait_words = ["r", "R", "retrait", "RETRAIT", "Retrait", "1"]

depot_words = ["d", "D", "depot", "DEPOT", "Depot","2"]

solde_words = ["s", "S", "SOLDE", "solde", "Solde", "3"]

with open ("clients.json", 'r') as f:
    clients = json.load (f)
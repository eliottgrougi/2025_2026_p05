import json

quitting_words = ["quit", "Quit", "q", "Q", "ciao", \
                  "bye", "byebye", "au revoir", "over", "quitter", "quitté"]

retrait_words = ["r", "R", "retrait", "RETRAIT", "Retrait"]

depot_words = ["d", "D", "depot", "DEPOT", "Depot"]

solde_words = ["s", "S", "SOLDE", "solde", "Solde"]

with open ("clients.json", 'r') as f:
    clients = json.load (f)
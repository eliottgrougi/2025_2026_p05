

#  Simulateur de Distributeur Automatique de Billets (DAB)

## Description :
Ce projet Python simule le comportement d’un **distributeur automatique de billets (DAB)**.  
Il permet à un utilisateur de :
-  S’identifier avec un **code PIN fictif**.
-  **Consulter son solde**.
-  **Déposer de l’argent**.
-  **Retirer de l’argent** (avec décomposition en billets de 50€, 20€, 10€, et 5€).
-  **Quitter le programme** proprement.

Toutes les données clients (nom, prénom, solde, code PIN, etc.) sont enregistrées dans un fichier `clients.json`.  
Les opérations de dépôt et retrait sont sauvegardées automatiquement.

---

## Fonctionnalités principales :

| Fonction | Description |

|  **Authentification** | Vérifie le code PIN dans le fichier `clients.json`. |
| **Dépôt** | Ajoute un montant au solde du compte et sauvegarde le fichier. |
|  **Retrait** | Vérifie le solde disponible, retire la somme demandée et affiche la décomposition en billets. |
|  **Consultation du solde** | Affiche le solde actuel du compte. |
|  **Quitter** | Termine proprement la session du client. |

---


### 1) Connexion

Au démarrage, le programme affiche :

```
============= BIENVENUE - PIOCHE BANQUE [PB] =============
Veuillez vous identifier en rentrant votre ID client (code PIN)
Ton id client:
```

=> Entrez votre identifiant (existant dans `clients.json`).
Si le code est invalide, le programme redemande la saisie.

---

### 2) Menu principal

Une fois connecté, le menu suivant s’affiche :

```
R : Retrait
D : Dépôt
S : Consulter le solde
Q : Quitter la banque
```

* Tapez **R** → pour effectuer un retrait (multiple de 5).
* Tapez **D** → pour faire un dépôt.
* Tapez **S** → pour consulter le solde.
* Tapez **Q** → pour quitter le programme.

Chaque modification est automatiquement enregistrée dans le fichier `clients.json`.

---

## Structure du projet :

main.py              # Code principal du programme
clients.json         # Données des clients (PIN, nom, solde)
README.md            # Manuel utilisateur

---

## Exemple de contenu du fichier `clients.json` :

```json
{
    "1234": {
        "prenom": "Théo",
        "nom": "Martin",
        "solde": 150
    },
    "5678": {
        "prenom": "Emma",
        "nom": "Dupont",
        "solde": 320
    }
}
```

---

## Exemple d’exécution :

```
------------ BIENVENUE - PIOCHE BANQUE PB -------------
Veuillez vous identifier en rentrant votre ID client (code PIN)
Ton id client: 1234
Bienvenue Théo Martin !
Ton solde est de 150 €.

Veuillez choisir les opérations à effectuer :
R : retrait
D : dépôt
S : consulter le solde
Q : quitter la banque

Entrez la commande : R
Combien veux-tu retirer ? 45

== Billets distribués : ==
0 billet(s) de 50 €
2 billet(s) de 20 €
0 billet(s) de 10 €
1 billet(s) de 5 €

Nouveau solde : 105 €
```

---

## Auteur :

Projet réalisé dans le cadre d’un projet Python en NSI – **Simulation d’un Distributeur Automatique de Billets (DAB)**.


```

Tom RENOU
Esteban GABILLA
Eliott GROUGI

NSI 
1er 2
2025-2026

```

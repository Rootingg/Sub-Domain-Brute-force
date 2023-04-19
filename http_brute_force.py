# BRUTE FORCE VIA HTTP

import requests

url_base = input("Domaine (exemple : google.fr) : ")
wordlist = input("Emplacement complet Fichier wordlist : ") #

with open(wordlist) as f:
    content = f.read().splitlines()

for sous_domaine in content:
    url = "http://"+sous_domaine+"."+url_base
    r = requests.get(url)
    if r.status_code == 200:
        print("Sous Domaine Trouver :  ",sous_domaine," Code Réponse ",r.status_code, " url accessible ",url)
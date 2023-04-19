# BRUTE FORCE VIA DNS

import dns.resolver

url_base = input("Domaine (exemple : google.fr) : ")
wordlist = input("Emplacement complet Fichier wordlist : ") 

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8', '8.8.4.4'] # IP RESEAU PRIVER PAR EXEMPLE POUR CTF HACK THE BOX OU AUTRES

with open(wordlist) as f:
    content = f.read().splitlines()

subdomains = []

for sous_domaine in content:
    url = sous_domaine + '.' + url_base
    try:
        answers = resolver.resolve(url)
        for rdata in answers:
            if url not in subdomains:
                subdomains.append(url)
                print("Sous Domaine Trouver : ", sous_domaine, " Adresse IP : ", rdata.address, " Serveur DNS : ", resolver.nameservers)
    except dns.resolver.NXDOMAIN:
        pass
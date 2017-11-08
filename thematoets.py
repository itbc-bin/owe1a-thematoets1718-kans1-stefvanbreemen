#auteur: Stef van Breemen
#datum: 08Nov2017

def main():
    list = []
    list = read(list)
    list = verifier(list)
    list = ions(list)

#input: csv bestand
#ouput: 2d lijst met acc code en variable.

def read(list):
    bestand = open("yeast_genes.csv")
    list = []
    for line in bestand:
        line = line.split(",")
        list.append(line)
    del(list[0])
    return list

#input: 2d lijst
#output: 2 lijsten, en met verified genes en een met unverified genes. 2 counting variables, een voor wel verified ander voor niet verified.
#omschrijving: kijk of er verified staat op het tweede plekje van de sublijst en voeg hierna toe aan toegepaste lijst en telt dan ook bij de variable een op.

def verifier(list):
    very = []
    vern = []
    y = 0
    n = 0

    for i in list:
        if i[1] == "Verified":
            very.append(i[0])
            y += 1
        else:
            vern.append(i[0])
            n += 1

    print("verified:    ",y, very)
    print("not Verified:", n, vern)
#input 2d lijst
#ouput lijst met genen waar ion bij staat.
# kijkt of er ion bij staat
def ions(list):
    ions = []
    ion = []

    for item in list:
        if item[1] != "Verified":
            ions.append(item)

    for item in ions:
        if item[2] == "ion":
            ion.append(item[0])
    return(ions)

main()
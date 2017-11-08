def main():
    list = []
    list = read(list)
    list = verifier(list)
    very = []
    vern = []
    #ions(list)
def read(list):
    bestand = open("yeast_genes.csv")
    list = []
    for line in bestand:
        line = line.split(",")
        list.append(line)
    del(list[0])
    return list


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


def ions(list):
    ions = []

    for i in list:
        if i[2] == "ion":
            ions.append(i[0])
    return(ions)

main()
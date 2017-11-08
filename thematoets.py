def main():
    list = []
    list = read(list)
    ver(list)
    print(list)


def read(list):
    bestand = open("yeast_genes.csv")
    list = []
    for line in bestand:
        line = line.split()
        list.append(line)
    return list

def ver(list):
    very = []
    vern = []
    for i in list:
        if i in list:
            if i[1] == "verified":
                very.append(i[0])
            else:
                vern.append(i[0])
    print("verified:", very)
    print("not Verified:", vern)
main()
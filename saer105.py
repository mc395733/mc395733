import csv
from matplotlib import pyplot as plt

def pop_2008(f):
    L=[]
    for ligne in open(f,"r",encoding="utf-8"):
        ligne=ligne.strip("\n").split(",")
        L.append(ligne)
    for x in L:
        if x[6]=="Auxerre":
            return int(x[9])

def pop_2016(f):
    L=[]
    for ligne in open(f,"r",encoding="utf-8"):
        ligne=ligne.strip("\n").split(",")
        L.append(ligne)
    for x in L:
        if x[6]=="Auxerre":
            return int(x[9])

def pop_2021(f):
    L=[]
    for ligne in open(f,"r",encoding="utf-8"):
        ligne=ligne.strip("\n").split(";")
        L.append(ligne)
    for x in L[1:]:
        if x[2]=="89024":
            return int(x[5])

def pop_2023(f):
    L=[]
    for ligne in open(f,"r",encoding="utf-8"):
        ligne=ligne.strip("\n").split(";")
        L.append(ligne)
    for x in L[1:]:
        if x[7]=="Auxerre":
            return int(x[10])

p2008=pop_2008("donnees_2008.csv")
p2016=pop_2016("donnees_2016.csv")
p2021=pop_2021("donnees_2021.csv")
p2023=pop_2023("donnees_2023.csv")

print(p2008, p2016, p2021, p2023)

annees=[2008,2016,2021,2023]
pops=[p2008,p2016,p2021,p2023]

plt.plot(annees,pops,marker="o")
plt.title("Population d'Auxerre")
plt.xlabel("Année")
plt.ylabel("Population totale")
plt.grid()
plt.show()

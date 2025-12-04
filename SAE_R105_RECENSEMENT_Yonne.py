import matplotlib.pyplot as plt

def yonne2008():
    L=[]
    for l in open("donnees_2008.csv","r",encoding="utf-8"):
        L.append(l.strip().split(","))
    s=0
    for x in L[1:]:
        if x[2]=="89":
            s+=int(x[9])
    return s

def yonne2016():
    L=[]
    for l in open("donnees_2016.csv","r",encoding="utf-8"):
        L.append(l.strip().split(","))
    s=0
    for x in L[1:]:
        if x[2]=="89":
            s+=int(x[9])
    return s

def yonne2021():
    L=[]
    for l in open("donnees_2021.csv","r",encoding="utf-8"):
        L.append(l.strip().split(";"))
    s=0
    for x in L[1:]:
        if x[1]=="89":
            s+=int(x[5])
    return s

def yonne2023():
    L=[]
    for l in open("donnees_2023.csv","r",encoding="utf-8"):
        L.append(l.strip().split(";"))
    s=0
    for x in L[1:]:
        if x[2]=="89":
            s+=int(x[10])
    return s

y2008=yonne2008()
y2016=yonne2016()
y2021=yonne2021()
y2023=yonne2023()

print("Yonne :", y2008, y2016, y2021, y2023)

annees=[2008,2016,2021,2023]
pops=[y2008,y2016,y2021,y2023]

plt.plot(annees,pops,marker="o")
plt.title("Population du département de l'Yonne")
plt.xlabel("Année")
plt.ylabel("Population totale")
plt.grid()
plt.show()

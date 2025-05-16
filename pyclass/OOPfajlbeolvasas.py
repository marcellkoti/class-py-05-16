import math
class Szavazatok:
    def __init__(self,korzet,szavazat,jeloltekcs: str,jeloltekut: str,part):
        self.korzet = int(korzet)
        self.szavazat = int(szavazat)
        self.jeloltekcs = jeloltekcs
        self.jeloltekut = jeloltekut
        self.part = part
        
    #def monogram(self):
        #return f"{}"

    def teljesnev(self):
        return f"{self.jeloltekcs} {self.jeloltekut}" 


    def __str__(self):
        return f"{self.korzet}, {self.szavazat}, {self.jeloltekcs},{self.jeloltekut}, {self.part}"

def Beolvasas(fajlnev):
    szavazas = []
    try:
        with open(fajlnev,"rt",encoding="utf-8") as file:
            #next(file)
            for sor in file:
                if sor.strip():
                    adat = sor.strip().split(" ")
                    #print(f"Beolvasott adatok: {adat}")
                    if len(adat) == 5:
                        try:
                            korzet,szavazat,jeloltekcs,jeloltekut,part = adat
                            szavazas.append(Szavazatok(korzet,szavazat,jeloltekcs,jeloltekut,part))
                        except ValueError:
                            print("Hibás adatsor")
                    else:
                        print("Hibás adatsor")
    except FileNotFoundError:
        print("A fájl nem lett megadva")
        return []
    return szavazas

szavazas = Beolvasas("szavazatok.txt")
for szavazat in szavazas:
    print(f"Körzet: {szavazat.korzet}, Szavazat: {szavazat.szavazat}, Jelöltek: {szavazat.jeloltekcs} {szavazat.jeloltekut}, Párt: {szavazat.part}")


print(f"A választáson {len(szavazas)}-en indultak")

#Hány érvényes szavazatot adtak le a választáson
ervenyes = sum(sz.szavazat for sz in szavazas)
print(ervenyes)
#Kérjen be egy pártot és irassa ki hogy a párt az adott párt választáson a szavazatok hány százalékát szerezte meg

#partb = input("Kérek egy pártot: ")
#talalat = any(t for t in szavazas if t.part.lower() == partb.lower())
#ossz = sum(talalat.szavazat)
#if talalat:
   #print(f" {ossz}  ez az összes szavazatnak a {round((100/ervenyes)*talalat.szavazat)}%-át teszi ki")
#else:
    #print("Nincs ilyen párt")




#Határozza meg a jelöltek Monogrammját!
for jelolt in szavazas:
    daraboltnev = jelolt.teljesnev().split(" ")
    print(f"{daraboltnev[0][0]} {daraboltnev[1][0]}")

#Listázzuk ki mely pártok indultak
#Minden párt csak egyszer szerepeljen

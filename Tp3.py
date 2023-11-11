# #Equatipn deuxieme degree
def descriminent(a, b, c):
    return b * b - 4 * a * a * c


def NombreRacine(a, b, c, x):
    test = 0
    if a * x * x + b * x + c == 0:
        test = 1
    return test


def AfficheNombreRacine(x):
    if x > 0:
        return 0
    elif x == 0:
        return 1
    else:
        return 2


def Racine1(a, b, x):
    return b - pow(x, 0.5) / 2 * a


def Racine2(a, b, x):
    return b + pow(x, 0.5) / 2 * b


a, b, c = print(input("Donner les coefficients a,b,c:"))
Delta = descriminent(1, 0, 0)
test = AfficheNombreRacine(Delta)
r1 = Racine1(1, 1, Delta)
r2 = Racine2(1, 1, Delta)
r = -0 / 1 * 1
if test == 0:
    print(f"les deux racines sont {r1} et {r2}")
elif test == 1:
    print(f"la racine est  {r}")
elif test == 2:
    print("La fonction n'a pas de solution dans R.")
# Conversion temps
h = int(input("Donner le nombre d'heurs"))
m = int(input("Donner le nombre de minute"))
s = int(input("Donner le nombre de seconde "))


def conversion_temps(h, m, s):
    return h * 3600 + m * 60 + s


print("conversion de {h}:{m}:{s}", conversion_temps(h, m, s))
# Temps ecoluer
h = int(input("Donner le nombre d'heurs :"))
m = int(input("Donner le nombre de minute :"))
s = int(input("Donner le nombre de seconde : "))
h1 = int(input("Donner le nombre d'heurs :"))
m1 = int(input("Donner le nombre de minute :"))
s1 = int(input("Donner le nombre de seconde  :"))


def conversion_temps(h, m, s):
    return h * 3600 + m * 60 + s


# print(f"Differece  de {h}H:{m}M:{s}S et {h1}H:{m1}M:{s1}S",conversion_temps(h,m,s)-conversion_temps(h1,m1,s1))
# Converstion distance
km = int(input("Donner la distance en kélemotre :"))
m = int(input("Donner la distance en métre :"))
cm = int(input("Donner la disatnce en centimétre :"))


def conversion_distance(km, m, cm):
    return km * pow(10, 3) + m + cm * pow(10, -2)


print(f"La conversion de distance {km}Km:{m}m:{cm}", conversion_distance(km, m, cm))
# Vitesse
h = int(input("Donner le nombre d'heurs :"))
m = int(input("Donner le nombre de minute :"))
s = int(input("Donner le nombre de seconde : "))
km = int(input("Donner la distance en kélemotre :"))
m = int(input("Donner la distance en métre :"))
cm = int(input("Donner la disatnce en centimétre :"))
print("La vitesse est :", conversion_distance(h, m, s) / conversion_temps(km, m, cm), "m/s")
# Programm zur Berechnung der Frequenzverhältnisse der verschiedenen
# Stimmungen. Ausgegebene Tabellen können mit dem_der Stimmungsmacher_in
# verwendet werden.
#
# Quellen: VO Allgemeine Musiklehre (Mag. S. Reisigl),
# Ziegenrückers "ABC Musik",
# https://de.wikipedia.org/wiki/Tonstruktur_(mathematische_Beschreibung)#Beispiele_ausf%C3%BChrlich (und dort bevorzugt die fettgedruckten Intervallbezeichnungen)

import math

print("\n\n# Gleichschwebend")
# Töne sind um den Faktor 12. Wurzel aus 2 voneinander entfernt
for k in range(0, 12):
    print(2 ** (k/12))

print("\n\n# Pythagoräisch")
# Töne ergeben sich aus reinen Quinten und Oktaven
# (f aus einer Quint hinunter, alle anderen Stammtöne r5 hinauf + r8 hinunter,
# Halbtöne mehrfache Vielfache (s. Wikipedia)).
pythagoräisch = [1.0, 256/243, 9/8, 32/27, 81/64, 4/3, 729/512, 3/2,
        128/81, 27/16, 16/9, 243/128]
for verhältnis in pythagoräisch:
    print(verhältnis)

print("\n\n# Rein")
# Töne leiten sich von Terz- und Quintproportion ab
rein = [1.0, 16/15, 9/8, 6/5, 5/4, 4/3, 45/32, 3/2, 8/5, 5/3, 16/9, 15/8]
for verhältnis in rein:
    print(verhältnis)

print("\n\n# Hammond")
# Töne gemäß Verhältnissen von Zahnrädern, Getrieben und Synchron-E-Motor
hammond_c = 85/104
hammond = [note/hammond_c for note in [85/104, 71/82, 67/73, 105/108,
    103/100, 84/77, 74/64, 98/80, 96/74, 88/64, 67/46, 108/70]]
for verhältnis in hammond:
    print(verhältnis)

print("\n\n# Obertöne")
# Töne aus der Obertonreihe
cis = 11/8 * 3/4 # Quint zu fis
f = 4/3 # Quint unter c
gis = cis * 3/2 # Quint zu cis
dis = 14/8 * 2/3 # Quart zu b
otr = [1.0, cis, 9/8, dis, 5/4, f, 11/8, 3/2, gis, 13/8, 14/8, 15/8]
for verhältnis in otr:
    print(verhältnis)


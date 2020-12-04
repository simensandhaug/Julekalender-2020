liste = open("leveringsliste.txt", "r").read().replace("\n", ",").replace(" ", "").split(",")
total = {"sukker":0, "mel":0, "melk":0, "egg":0}

for el in liste:
    sections = el.split(":")
    total[sections[0]] += int(sections[1])

print(min([total["sukker"] // 2, total["mel"] // 3, total["melk"] // 3, total["egg"] // 1]))
import random

first_names=('Sebastian','Monika','Krystian','Sandra','Marek','Marlena','Jolanta','Albert','Agata','Laura','Waldemar','Jerzy','Zygmunt','Joanna','Irena','Dorota','Grażyna','Karolina','Sylwia','Patrycja','Aneta','Jan','Tomasz','Adam','Kamil','Jacek','Mariusz')
last_names=('Gliszczyński','Bilicki','Smoter','Janeczko','Janas','Brodowski','Włosek','Gancarz','Zelek','Synowiec','Kaptur','Połomski','Długosz','Śmiech','Nocoń','Wiśniewski','Wójcik','Zieliński','Jankowski','Kwiatkowski','Kaczmarek','Mazur','Pawłowski','Olszewski','Rutkowski','Ostrowski','Tomaszewski','Szulc','Sikorski','Kołodziej','Czerwiński','Lis','Maciejewski','Włodarczyk','Baran','Górski','Malinowski','Jabłoński','Adamczyk','Pawłowski','Piotrowski','Kozłowski','Kamiński','Dąbrowski',)
group=" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(3))


print(group)
cuginetta = ["Marta", "Nina", "Elisa"]
cuginetto = ["Davide", "Giacomo", "Andrea"]

dove = ["sulla Luna","a Parigi", "in via Sestri" ]
vestitoCuginetta = ["un vestito da principessa", "una gonnellina scozzese", "un vestito da sera" ]
vestitoCuginetto = ["un costume da ninja", "la maglia del PSG", "delle corna da vichingo" ]
cuginettaDice = ["Oh! che bel vestito!", "Sono la piu chic", "Non sembro la nonna Gio?" ]
cuginettoDice = ["Sono un vichingo", "Che bel gol!", "Dove vai?" ]
conseguenza = ["una enorme esplosione.", "una puzza pazzesca.", "il portiere ha pianto." ]
laGente = ["Questi sono pazzi!", "Poveracci...", "Quelli li' sono ricchi.", "Tornate a scuola!"]

import random
while True:
    print(random.choice(cuginetta), "ha incontrato", random.choice(cuginetto), random.choice(dove))
    print("La cuginetta indossava ", random.choice(vestitoCuginetta))
    print("Il cuginetto indossava ", random.choice(vestitoCuginetto))
    print("La cuginetta ha detto", random.choice(cuginettaDice))
    print("Il cuginetto ha detto", random.choice(cuginettoDice))
    print("La conseguenza e' stata ", random.choice(conseguenza))
    print("La gente ha detto", random.choice(laGente))

    print()
    input("Schiaccia su INVIO per rigiocare.")
    print()

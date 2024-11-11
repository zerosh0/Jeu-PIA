# Showcase des Animations avec Pygame


Ce projet est une démonstration de la façon dont on peut réaliser des animations de sprites dans un jeu en utilisant Pygame. L'animation est réalisée en découpant une image de sprite (spritesheet) et en la parcourant pour afficher les différentes frames d'une animation.

## Structure du projet

/Jeu PIA  
├── main.py              # Point d'entrée du jeu, gestion du boucle de jeu et des événements  
├── players.py           # Définition de la classe Player, gestion des animations et des déplacements  
├── spritesheet.py       # Classe pour charger et découper une spritesheet en animations  
├── Assets/Images        # Dossier contenant les images de sprites  
│   └── kirby.png        # Image de spritesheet de Kirby  
└── README.md            # Documentation du projet  
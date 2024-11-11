import pygame

class SpriteSheet:
    def __init__(self, filename, colorkey):
        self.sprite_sheet = pygame.image.load(filename).convert() #charge l'image du spritesheet .convert() optimise le chargement
        self.colorkey = colorkey #couleur de fond pour la transparence 
        self.animations = {} #dictionnaire avec les animations clé=nom de l'animation valeur=liste des images d'animations

    def add_animation(self, name, frames_data,scale=1.0):
        """
        Ajoute une animation au dictionnaire.
        
        name : nom de l'animation (ex: 'run', 'idle')
        frames_data : liste de tuples (x, y, width, height) pour chaque frame de l'animation
        scale : redimensionnement de l'image
        """
        frames = []
        for (x, y, width, height) in frames_data:
            image = pygame.Surface((width, height)).convert() #créer une surface (comme un écran aux dimensions de la frame), .convert() permet d'optimiser le chargement 
            image.blit(self.sprite_sheet, (0, 0), (x, y, width, height)) #imprime l'image du spritesheet en découpant le rectangle qui correspond à l'image de l'animation (x, y, width, height)
            image.set_colorkey(self.colorkey)  # Appliquer la couleur de fond pour la transparence
            image=pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale))) #redimensionne l'image si besoin
            frames.append(image)
        self.animations[name] = frames

    def get_animation(self, name):
        """Retourne la liste de frames pour une animation donnée."""
        return self.animations.get(name, []) #retourne la liste des images pour un nom donné du dictionnaire animation, si le nom n'existe pas retourne []

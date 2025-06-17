import pygame 

class Points_counter(pygame.sprite.Sprite):
    def __init__(self, x, y, font,size, points):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.x = x
        self.y = y
        self.font = font
        self.size = size
        self.points = points
        
    def draw(self, screen):
        Font = pygame.font.Font(self.font,self.size) 
        text_surface = Font.render(f"Points: {self.points}",False,"white")
        screen.blit(text_surface,(self.x,self.y))

    def update(self, added_points):
        self.points += added_points
        
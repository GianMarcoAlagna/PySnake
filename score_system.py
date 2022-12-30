class Score:
    def __init__(self, game):
        self.score = 0
        self.font = game.font.SysFont("Arial.tff", 35)
        self.text = self.font.render("Score: {0}".format(self.score),1,(25,25,25))
    
    def inc_score(self):
        self.score += 1
        self.text = self.font.render("Score: {0}".format(self.score),1,(25,25,25))
    
    def display_score(self,surface):
        surface.blit(self.text,(10,10))
    
    def reset(self):
        self.score = 0
        self.text = self.font.render("Score: {0}".format(self.score),1,(25,25,25))
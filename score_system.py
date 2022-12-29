class Score:
    score = 0
    def __init__(self, game):
        self.font = game.font.SysFont("Arial.tff", 35)
        self.text = self.font.render("Score: {0}".format(self.score),1,(25,25,25))
    
    def inc_score(self):
        self.score += 1
        self.text = self.font.render("Score: {0}".format(self.score),1,(25,25,25))
    
    def display_score(self,surface):
        surface.blit(self.text,(10,10))

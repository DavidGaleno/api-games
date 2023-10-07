from game import Game

class GameFan(Game):
    trailer: str
    the_game_awards_awards: []
    buy_links: []
    expansions: []
    dlcs: []
    actors: []

    def __init__(self,trailer,the_game_awards_awards,buy_links,expansions,dlcs,actors):
        self.trailer = trailer
        self.the_game_awards_awards = the_game_awards_awards
        self.buy_links = buy_links
        self.expansions = expansions
        self.dlcs = dlcs
        self.actors = actors
    
    
    def get_mean_price():
        pass
    def get_reviews():
        pass
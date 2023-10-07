from game import Game

class GameAccountant(Game):
    production_cost: float
    marketing_cost: float
    total_physical_copies_sold: float
    total_digital_copis_sold: float
    mean_score: float

    def __init__(self, production_cost, marketing_cost, total_physical_copies_sold, total_digital_copies_sold, mean_score):
        self.production_cost = production_cost
        self.marketing_cost = marketing_cost
        self.total_digital_copis_sold = total_digital_copies_sold
        self.total_physical_copies_sold = total_physical_copies_sold
        self.mean_score = mean_score

    def get_billing():
        pass
    def get_currently_players_amount():
        pass

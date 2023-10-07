from game import Game

class game_developer(Game):
    programming_language: str
    engine: str
    anti_cheat_software: str
    modeling_software: str
    minimum_requirements: str
    recommended_requirements: str

    def __init__(self, programming_language, engine, anti_cheat_software, modeling_software, minimum_requirements, recommended_requirements):
        self.programming_language = programming_language
        self.engine = engine
        self.anti_cheat_software = anti_cheat_software
        self.modeling_software = modeling_software
        self.minimum_requirements = minimum_requirements
        self.recommended_requirements = recommended_requirements
    
    def get_job_opportunities():
        pass

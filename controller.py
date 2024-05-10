from model import Model
from view import OthelloView

class OthelloController:
    def __init__(self):
        self.model = Model()
        self.view = OthelloView(self)

    
    def start_game(self):
        pass
    

    def on_click(self):
        pass
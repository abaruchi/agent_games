from player import Player

class CustomPlayer(Player):

    def make_decision(self, game_state):
        if game_state["roll_no"] == 3:
            return 'bank'
        return 'continue'
from games.prisoners_dilemma.player import Player

class CustomPlayer(Player):
    def make_decision(self, game_state):
        my_opponent = game_state["opponent_name"]
        opponent_history = game_state["opponent_history"]
        my_history = game_state["my_history"]
        #print(f"my opponent is {my_opponent} his moves were {opponent_history} against my moves {my_history}")


        return 'defect'
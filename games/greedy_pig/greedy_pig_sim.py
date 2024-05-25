from games.greedy_pig.greedy_pig import Game
from models import League
import os
import time

def draw_table(rankings):
    os.system('clear')
    print("-" * 50)
    print(f"{'Player':^20} | {'Points':^10} | {'Rank':^10}")
    print("-" * 50)
    for rank, (player, points) in enumerate(rankings, start=1):
        print(f"{player:^20} | {points:^10} | {rank:^10}")
    print("-" * 50)
    time.sleep(0.3)

def animate_simulations(num_simulations, refresh_number, game):
    
    total_points = dict()
    for player in game.players:
        print(player.name)
        total_points[player.name] = 0
    
    for i in range(1, num_simulations + 1):
        game.reset()
        # reset happens here
        results = game.play_game()
        
        for player, points in results["points"].items():
            total_points[player] += points
        
        if i % refresh_number == 0 or i == num_simulations:
            print(f"\nRankings after {i} simulations:")
            sorted_total_points = sorted(total_points.items(), key=lambda x: x[1], reverse=True)
            draw_table(sorted_total_points)

        
def run_simulations(num_simulations, league):
    #league.folder is relative path
    game = Game(league)
    print("Players", game.players)
    #create a dictionary to store the total points for each player
    total_points = dict()
    for player in game.players:
        print(player.name)
        total_points[player.name] = 0
    print("Total Points", total_points)
    try:
        for i in range(1, num_simulations + 1):
            game.reset()
            results = game.play_game()
            for player, points in results["points"].items():
                total_points[player] += points
    
    except Exception as e:
        raise Exception(f"Simulation failed: {str(e)}")
    
    sorted_total_points = sorted(total_points.items(), key=lambda x: x[1], reverse=True)
    
    return dict(sorted_total_points)
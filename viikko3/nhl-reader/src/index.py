import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )

        players.append(player)

    players.sort(key=lambda player: player.goals+player.assists, reverse=True)

    print("Players from Finland:\n")
    
    for player in players:
        if player.nationality == 'FIN':
            print(player)

if __name__ == "__main__":
    main()
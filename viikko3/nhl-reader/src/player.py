from re import template
import requests


class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
    
    def __str__(self):
        return f'{self.name:20} {self.team:3} {self.goals:2} + {self.assists:2} = {self.goals+self.assists:2}'

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []

    def get_players(self):
        response = requests.get(self.url).json()

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists']
            )

            self.players.append(player)
        return self.players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = [player for player in self.players if player.nationality==nationality]
        players.sort(key=lambda player: player.goals+player.assists, reverse=True)
        return players

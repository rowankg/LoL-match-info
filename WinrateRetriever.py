import requests, json
import requests.exceptions


api_token = "RGAPI-fda5cdb6-a2e6-4726-aa04-ebefb203f01e"

class Summoner:

    def __init__(self, summoner_id=0, champion_id=0, summoner_name=0, team=0):
        self.summoner_name = summoner_name
        self.summoner_id = summoner_id
        self.champion_id = champion_id
        self.team = team

    def set_summoner_data(self, summoner_id, champion_id, summoner_name, team):
        self.summoner_name = summoner_name
        self.summoner_id = summoner_id
        self.champion_id = champion_id
        self.team = team

    def set_match_data(self, game_id, total_games, games_won):
        self.game_id = game_id
        self.total_games = total_games
        self.games_won = games_won


def get_account_id(summonerName):
    r = requests.get(createUrl(summonerName))
    account_id = r.json()['accountId']
    return account_id

def get_summoner_id(summonerName):
    r = requests.get(createUrl(summonerName))
    summoner_id = r.json()['id']
    return summoner_id

def createUrl(summonerName):
    url = "https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + api_token
    return url

def get_champion_by_id(account_id):
    url = "https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + str(account_id) + "/recent?api_key=" + api_token
    r = requests.get(url)
    # print(r.json())
    match = r.json()['matches'][0]
    champion_id = match['champion']


def get_current_match(summoner_id):
    url = "https://euw1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/" + str(summoner_id) + "?api_key=" + api_token
    r = requests.get(url)
    participants = r.json()['participants']
    summonerData = []
    for participant in participants:
        summoner_name = participant['summonerName']
        participant_id = participant['summonerId']
        champion_id = participant['championId']
        team = participant['teamId']
        summoner = Summoner()
        summoner.set

        summonerData.append(summoner)
        print(summoner_name, participant_id, champion_id, team)
    return summonerData


def get_champion_data(championId):
    return 0


def main():
    summoner_id = get_summoner_id("KOONEIN")
    print(summoner_id)
    account_id = get_account_id("KOONEIN")
    print(account_id)
    get_current_match(summoner_id)


if __name__ == "__main__":
    main()
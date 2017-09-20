import requests, json
import requests.exceptions

api_token = "RGAPI-ee86b79a-294f-436c-940b-341086c8cdb4"
api_base_url = "https://euw1.api.riotgames.com/lol/"
summoner_name = "Justaz"
season = 9

class Summoner:
    def __init__(self, summoner_id=0, champion_id=0, summoner_name=0, team=0):
        self.summoner_name = summoner_name
        self.summoner_id = summoner_id
        self.champion_id = champion_id
        self.team = team

    def set_summoner_data(self, summoner_id, champion_id, summoner_name, team, account_id):
        self.summoner_name = summoner_name
        self.summoner_id = summoner_id
        self.champion_id = champion_id
        self.team = team
        self.account_id = account_id

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
    print(createUrl(summonerName))
    summoner_id = r.json()['id']
    return summoner_id


def createUrl(summonerName):
    url = "https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + api_token
    return url


def createUrl2(*args):
    url = api_base_url
    for arg in args:
        url = url + str(arg)
    url = url + "?api_key=" + api_token
    return url


def createUrl3(api_path, *input_params):
    """
    This function is used to create a url by doing the following:
    1. Create url containing base url and the path to specific api
    2. Add each input argument to url
    3. Add api key to url
    The created url is then returned
    """
    url = api_base_url + api_path
    for input_param in input_params:
        url = url + str(input_param) + "&"

    # Remove last & from url
    url = url[:-1]

    url = url + "?api_key=" + api_token
    return url


def get_champion_by_id(champion_id):
    url = createUrl3("static-data/v3/champions/", champion_id)
    r = requests.get(url)
    champion_info = r.json()
    champion_id = champion_info['name']
    return champion_id


def get_current_match(summoner_id):
    url = "https://euw1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/" + str(
        summoner_id) + "?api_key=" + api_token
    r = requests.get(url)
    participants = r.json()['participants']
    summonerData = []
    for participant in participants:
        summoner_name = participant['summonerName']
        participant_id = participant['summonerId']
        champion_id = participant['championId']
        team = participant['teamId']
        account_id = get_account_id(summoner_name)


        summoner = Summoner()
        summoner.set_summoner_data(summoner_id, champion_id, participant_id, team, account_id)

        # get match history for every participant
        get_match_history_by_account_id(summoner, season, account_id, champion_id)

        summonerData.append(summoner)
        print(summoner_name, participant_id, champion_id, team, account_id)
    return summonerData


def get_champion_data(championId):
    return 0


def get_match_history_by_account_id(summoner, season, account_id, champion_id):
    url = "https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + str(account_id) + "?season=" + str(season) +\
          "&champion=" + str(champion_id) + "&api_key=" + api_token

    r = requests.get(url)
    game_id = []
    if r.ok:
        for match in r.json()["matches"]:
            game_id.append((match['gameId']))
            # make url for every match with match id and check if won or not,
            #if match won, games_won ++
        total_games = r.json()['totalGames']
        print(total_games)
    else:
        game_id = []
        total_games = 0



        # summoner.set_match_data(game_id, total_games, games_won)

def main():
    summoner_id = get_summoner_id(summoner_name)
    print(summoner_id)
    account_id = get_account_id(summoner_name)
    print(account_id)
    get_current_match(summoner_id)


if __name__ == "__main__":
    main()

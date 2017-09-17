import requests, json
import requests.exceptions


api_token = "RGAPI-3fcf1609-fd71-4199-848f-f0252c36255d"

class Summoner:

     def __init__(self, summoner_id, champion_id, summoner_name, team):
         self.summoner_name = summoner_name
         self.summoner_id = summoner_id
         self.champion_id = champion_id
         self.team = team

def get_account_id(url):

    r = requests.get(url)
    account_id = r.json()['accountId']
    return account_id

def get_summoner_id(url):
    r = requests.get(url)
    summoner_id = r.json()['id']
    return summoner_id

def createUrl(summonerName):
    url = "https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summonerName + "?api_key=" + api_token
    return url

def get_champion_by_id(account_id):
    url = "https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + str(account_id) + "/recent?api_key=RGAPI-3fcf1609-fd71-4199-848f-f0252c36255d"
    r = requests.get(url)
    # print(r.json())
    match = r.json()['matches'][0]
    champion_id = match['champion']
    print(champion_id)


def get_current_match(summoner_id):
    url = "https://euw1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/" + str(summoner_id) + "?api_key=RGAPI-3fcf1609-fd71-4199-848f-f0252c36255d"
    r = requests.get(url)
    print(url)
    participants = r.json()['participants']
    summonerData = []
    for participant in participants:
        summoner_name = participant['summonerName']
        participant_id = participant['summonerId']
        champion_id = participant['championId']
        team = participant['teamId']
        summoner = Summoner(participant_id, champion_id, summoner_name, team)

        summonerData.append(summoner)
        print(summoner_name, participant_id, champion_id, team)
    return summonerData



def get_champion_data(championId):



def main():
    summoner_url = createUrl("sjookie")
    summoner_id = get_summoner_id(summoner_url)
    get_current_match(summoner_id)


if __name__ == "__main__":
    main()
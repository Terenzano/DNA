import requests
import json

token = 'ZjE4ZWRhMjEtNzRmYy00NGY5LWEzZDEtNWFjYmFlM2IzYjE4OTNlMzBjY2UtMzA2_PF84_consumer'

### DELETE ROOM ###
room_url = 'https://api.ciscospark.com/v1/rooms'
headers = {'Authorization': f'Bearer {token}',
           'Content-Type': 'application/json'}


get_rooms = requests.get(room_url, headers=headers).json()

rooms = get_rooms['items']
for room in rooms:
    if room['title'] == 'CBT Room':
        roomId = room['id']
del_room_url = f'{room_url}/{roomId}'
del_room = requests.delete(del_room_url, headers=headers)


####### DELETE TEAM ##############
url = 'https://api.ciscospark.com/v1/teams'

get_response = requests.get(url, headers=headers).json()

teams = get_response['items']
for team in teams:
    if team['name'] == 'CBT Team':
        teamId = team['id']
del_team_url = f'{url}/{teamId}'
del_team = requests.delete(del_team_url, headers=headers)

import subprocess
import datetime
import requests
import time
import json
import os

#abstracted for simpler recreation
#TODO: Simplfiy the process of setting the git user name and token?
GIT_USERNAME = 'RachelBethke'
GIT_TOKEN = os.environ.get('GITHUB_TOKEN')
INTERVAL = 60  # sec between polling (?)

# GIT_TOKENS = {  for when I use multiple tokens for school and personal git
#     # gives access to private and public commit data 
#     'rachelbethke' : 'GITHUB_TAMA_TOKEN' 
#     #add rkb76 later
# }

# push data getter
def get_last_push():
    """
    Getter to load the last push info from a file
    """
    headers = { 'authorization' : f'token {GIT_TOKEN}',
        'Accept': 'application/vnd.github.v3+json',
    }
    url = f'https://api.github.com/users/{GIT_USERNAME}/events'
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("error fetching")
        return None
    events = response.json()

    for i in events:
        if i['type'] == 'PushEvent':
            return events
        return None
    
# def save_last_push():
#     """
#     Save the last processed push info to a file
#     """
#     pass
def watch_pushes(callback):
    """ Waching for push events to trigger events when needed"""
    last_event = None
    while True:
        event = get_last_push()
        if event and event['id'] != last_event:
            last_event = event['id']
            callback()
        time.sleep(INTERVAL)

def process_push(push, un):
    """
    Process new push data to update current state file
    """
    pass

def update_log():
    """ 
    Update git log on the INTERVAL (minute) to reflect state
    """
    pass

if __name__ == '__main__':
    watch_pushes(lambda: print("callback"))

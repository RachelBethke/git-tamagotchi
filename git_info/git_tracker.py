import subprocess
import datetime
import requests
import time
import json
import os

GIT_TOKENS = { 
    # gives access to private and public commit data 
    'rachelbethke' : 'GITHUB_TOKEN_USERNAME' 
    #add rkb76 later
}

INTERVAL = 60 #seconds between polling (?)
PUSH_LOG= 'push_events.log'
LAST_PUSH= "last_event_ids.json"

# push data getter
def get_last_push():
    """
    Getter to load the last push info from a file
    """
    if os.path.exists(LAST_PUSH):
        with open(LAST_PUSH, 'r') as f:
            return json.load(f)
    else: return {}
        
# def save_last_push():
#     """
#     Save the last processed push info to a file
#     """
#     pass

def process_push(push, un):
    """
    Process new push data to update current state file
    """
    pass

def update_log():
    """ 
    Update git log on the INTERVAL (minute) to reflect state
    """

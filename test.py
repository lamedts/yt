# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import google.oauth2.credentials
import json

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# 4/sQEtTEdSJbc1ltTuvPNBnlXUjBtTQzAtx1mim2DtMmMsXQ7fro6JFcM
youtube = None

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    credentials = None
    
    if os.path.isfile('cred.json'):
        with open('cred.json', encoding='utf-8') as json_file:
            credentials = google.oauth2.credentials.Credentials(json.load(json_file))
    else:
        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
        credentials = flow.run_console()
        with open('cred.json', 'w', encoding='utf8') as json_file:
            creds_data = credentials_to_dict(credentials)
            del creds_data['token']
            json.dump(creds_data, json_file)

    
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId="FLxG7RVKBhVK2UMyCwFWnASA",
        maxResults=50
    )
    response = request.execute()

    return 
    highscore = open('text.txt','a')
    highscore.write(json.dumps(response['items']))
    highscore.write('\n')
    highscore.close()
    if 'nextPageToken' in response:
        next_page(response['nextPageToken'], youtube)

def next_page(next_page_token, youtube):
    request = youtube.playlistItems().list(
        part="snippet",
        playlistId="FLxG7RVKBhVK2UMyCwFWnASA",
        maxResults=50,
        pageToken=next_page_token
    )
    response = request.execute()

    highscore = open('text.txt','a')
    highscore.write(json.dumps(response['items']))
    highscore.write('\n')
    highscore.close()

    if 'nextPageToken' in response:
        next_page(response['nextPageToken'], youtube)

def credentials_to_dict(credentials):
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}

if __name__ == "__main__":
    main()
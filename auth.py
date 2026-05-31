import os
import json
from stravalib.client import Client 

TOKEN_FILE = ".strava_token.json"

def get_client():
    client - Client()

    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            token_data = json.load(f)
    client.access_token = token_data["access_token"]
    client.refresh_token = token_data["refresh_token"]
    client.token_expires_at = token_data["expires at"]
    return client

    client_id = os.getenv("STRAVA_CLIENT_ID")
    client_secret = os.getenv("STRAVE_CLIENT_SECRET")

    url = client.authorization_url(
        client_id=client_id,
        redirect_url="http://localhost:8000/callback"
    )

    print(f"Open this URL in your browser:\n{url}")
    code = input("\nPaste the code from the redirect URL: ")

    token_response = client.exchange_code_for_token(
        client_id=client_id,
        client_secret=client_secret,
        code=code
    )

    with open(TOKEN_FILE, "w") as f:
        json.dump(token_respone, f)

    return client

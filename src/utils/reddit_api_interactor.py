import requests, json
from secrets import REDDIT_API_TOKEN, REDDIT_API_CLIENT_ID, REDDIT_USERNAME, REDDIT_PASSWORD


class RedditAPI:
    def __init__(self, token, client_id, username, password):
        auth = requests.auth.HTTPBasicAuth(client_id, token)
        data = {'grant_type': 'password',
                'username': username,
                'password': password}

        headers = {'User-Agent': 'MyBot/0.0.1'}
        
        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=auth, data=data, headers=headers)
        
        TOKEN = res.json()['access_token']
        self.headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

        # while the token is valid (~2 hours) we just add headers=headers to our requests
        requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

    def get_headers(self, subreddit):
        res = requests.get(subreddit,
                        headers=self.headers)

        with open("temp.json", "w") as outfile:
            json_obj = json.dumps(res.json(), indent=2)
            outfile.write(json_obj)

if __name__ == "__main__":
    print("Executing Reddit_api_interactor.py")
    reddit_api = RedditAPI(REDDIT_API_TOKEN, REDDIT_API_CLIENT_ID, REDDIT_USERNAME, REDDIT_PASSWORD)
    reddit_api.get_headers("https://oauth.reddit.com/r/wallstreetbets/hot")

    
import requests
from secrets import Reddit_API_SECRET, Reddit_API_Personal_Use_Script, Username, Password


class FinnhubAPI:
    # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
    auth = requests.auth.HTTPBasicAuth(Reddit_API_Personal_Use_Script, Reddit_API_SECRET)

    # here we pass our login method (password), username, and password
    data = {'grant_type': 'password',
            'username': Username,
            'password': Password}

    # setup our header info, which gives reddit a brief description of our app
    headers = {'User-Agent': 'MyBot/0.0.1'}

    # send our request for an OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    # convert response to JSON and pull access_token value
    TOKEN = res.json()['access_token']


    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    # while the token is valid (~2 hours) we just add headers=headers to our requests
    requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

    res = requests.get("https://oauth.reddit.com/r/python/hot",
                    headers=headers)

    print(res.json())  # let's see what we get

if __name__ == "__main__":
    print("Executing Reddit_api_interactor.py")
    
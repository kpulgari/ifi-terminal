import requests, json, praw

if __name__ == "__main__":
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

        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=token,
            password=password,
            user_agent="testing",
            username=username,
        )   

    def get_headers(self, subreddit) -> None:
        res = requests.get(subreddit,
                        headers=self.headers)

        with open("temp.json", "w") as outfile:
            json_obj = json.dumps(res.json(), indent=2)
            outfile.write(json_obj)

    def get_hot_posts(self, subreddit, limit):
        sub = self.reddit.subreddit(subreddit)
        hot_posts = sub.hot(limit=limit)
        hot_posts_arr = [post for post in hot_posts]
        return hot_posts_arr
    
    def get_post_top_comments(self, post, limit):
        submission = self.reddit.submission(post.id)
        submission.comments.replace_more(limit=50)
        comments = submission.comments.list()
        top_comments = sorted(comments, key=lambda comment: comment.score, reverse=True)[:limit]
        top_comments_arr = [comment for comment in top_comments]
        return top_comments_arr

if __name__ == "__main__":
    print("Executing Reddit_api_interactor.py")
    reddit_api = RedditAPI(REDDIT_API_TOKEN, REDDIT_API_CLIENT_ID, REDDIT_USERNAME, REDDIT_PASSWORD)
    post_arr = reddit_api.get_hot_posts("wallstreetbets", 10)
    reddit_api.get_post_top_comments(post_arr[0], 5)
    